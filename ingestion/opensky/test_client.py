import json
from datetime import datetime, timezone
from pathlib import Path

import requests


URL = "https://opensky-network.org/api/states/all"

OUTPUT_DIR = Path("data/raw/opensky")
OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def main():
    print("Connecting to OpenSky...")

    response = requests.get(
        URL,
        timeout=15,
    )

    print(f"HTTP Status: {response.status_code}")

    response.raise_for_status()

    data = response.json()

    states = data.get("states") or []

    print("\nSuccessfully received data from OpenSky!")
    print(f"Aircraft received: {len(states)}")

    timestamp = datetime.now(
        timezone.utc
    ).strftime("%Y%m%d_%H%M%S")

    output_file = (
        OUTPUT_DIR /
        f"opensky_{timestamp}.json"
    )

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=2,
        )

    print(f"\nData saved to:")
    print(output_file.resolve())


if __name__ == "__main__":
    main()