develop:
	docker-compose up --build

precommit:
	pre-commit run --all-files

.PHONY: develop precommit
