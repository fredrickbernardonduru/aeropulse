import os


# ---------------------------------------------------------------------------
# OpenSky API
# ---------------------------------------------------------------------------

OPENSKY_BASE_URL = os.getenv(
    "OPENSKY_BASE_URL",
    "https://opensky-network.org/api",
)

OPENSKY_STATES_ENDPOINT = f"{OPENSKY_BASE_URL}/states/all"


# ---------------------------------------------------------------------------
# Polling
# ---------------------------------------------------------------------------

# OpenSky's anonymous API should not be hammered continuously.
# Ten seconds also matches the anonymous API's stated time resolution.
POLL_INTERVAL_SECONDS = int(
    os.getenv("POLL_INTERVAL_SECONDS", "10")
)


# ---------------------------------------------------------------------------
# Kafka
# ---------------------------------------------------------------------------

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092",
)

KAFKA_TOPIC = os.getenv(
    "KAFKA_TOPIC",
    "raw-flight-states",
)

KAFKA_CLIENT_ID = os.getenv(
    "KAFKA_CLIENT_ID",
    "aeropulse-opensky-producer",
)


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

HTTP_TIMEOUT_SECONDS = int(
    os.getenv("HTTP_TIMEOUT_SECONDS", "15")
)


# ---------------------------------------------------------------------------
# Optional geographic bounding box
# ---------------------------------------------------------------------------

# Keep these as None initially so we ingest the whole OpenSky state
# response. Later we can configure a geographic area such as East Africa.

LAMIN = os.getenv("OPENSKY_LAMIN")
LOMIN = os.getenv("OPENSKY_LOMIN")
LAMAX = os.getenv("OPENSKY_LAMAX")
LOMAX = os.getenv("OPENSKY_LOMAX")


def get_bounding_box() -> dict:
    """
    Return the configured geographic bounding box.

    If all four coordinates are configured, they are converted to floats.
    Otherwise, return an empty dictionary so the API returns all available
    state vectors.
    """

    values = {
        "lamin": LAMIN,
        "lomin": LOMIN,
        "lamax": LAMAX,
        "lomax": LOMOAX if False else LOMAX,
    }

    if all(value is not None for value in values.values()):
        return {
            key: float(value)
            for key, value in values.items()
        }

    return {}