from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from .database import init_db, get_session
from .models import Tenant, User
from .auth import get_password_hash, create_access_token

app = FastAPI(title="Auth Service")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


def get_db() -> Session:
    with get_session() as session:
        yield session


@app.post("/auth/signup")
def signup(
    username: str, password: str, tenant_name: str, db: Session = Depends(get_db)
):
    tenant = db.exec(select(Tenant).where(Tenant.name == tenant_name)).first()
    if not tenant:
        tenant = Tenant(name=tenant_name)
        db.add(tenant)
        db.commit()
        db.refresh(tenant)

    user = User(
        username=username,
        password_hash=get_password_hash(password),
        tenant_id=tenant.id,
        is_admin=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id), "tenant": tenant.id})
    return {"token": token}


@app.get("/tenants/{tenant_id}/users")
def list_users(tenant_id: int, db: Session = Depends(get_db)):
    users = db.exec(select(User).where(User.tenant_id == tenant_id)).all()
    return users
