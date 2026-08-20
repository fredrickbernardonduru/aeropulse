from datetime import datetime, timezone
from typing import Any


STATE_VECTOR_FIELDS = [
    "icao24",
    "callsign",
    "origin_country",
    "time_position",
    "last_contact",
    "longitude",
    "latitude",
    "baro_altitude",
    "on_ground",
    "velocity",
    "true_track",
    "vertical_rate",
    "sensors",
    "geo_altitude",
    "squawk",
    "spi",
    "position_source",
    "category",
]


def parse_state_vector(
    state: list[Any],
    response_time: int,
) -> dict[str, Any]:
    """
    Convert one OpenSky state vector from an array into a dictionary.
    """

    values = list(state)

    # OpenSky may omit trailing fields depending on the response.
    if len(values) < len(STATE_VECTOR_FIELDS):
        values.extend(
            [None] * (
                len(STATE_VECTOR_FIELDS) - len(values)
            )
        )

    record = {
        field: values[index]
        for index, field in enumerate(STATE_VECTOR_FIELDS)
    }

    record["source"] = "opensky"

    record["ingestion_time"] = datetime.now(
        timezone.utc
    ).isoformat()

    record["response_time"] = response_time

    return record


def parse_response(
    response: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Parse an entire OpenSky API response.

    Returns a list of normalized aircraft state records.
    """

    response_time = response.get("time")

    states = response.get("states") or []

    parsed_records = []

    for state in states:
        if not state:
            continue

        record = parse_state_vector(
            state=state,
            response_time=response_time,
        )

        parsed_records.append(record)

    return parsed_records