import argparse


def main():
    parser = argparse.ArgumentParser(description="Ingestion worker")
    parser.add_argument("--source", required=True)
    parser.add_argument("--tenant", required=True)
    args = parser.parse_args()

    print(f"Ingesting {args.source} for tenant {args.tenant}...")
    # placeholder logic
    print("done")


if __name__ == "__main__":
    main()
