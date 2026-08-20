import logging
from typing import Any

import requests

from .config import (
    HTTP_TIMEOUT_SECONDS,
    OPENSKY_STATES_ENDPOINT,
    get_bounding_box,
)


logger = logging.getLogger(__name__)


class OpenSkyClient:
    """
    Client responsible for communicating with the OpenSky REST API.
    """

    def __init__(self) -> None:
        self.session = requests.Session()

    def get_states(self) -> dict[str, Any]:
        """
        Retrieve the latest aircraft state vectors from OpenSky.

        Returns
        -------
        dict
            OpenSky JSON response.

        Raises
        ------
        requests.RequestException
            If the HTTP request fails.
        """

        params = get_bounding_box()

        logger.debug(
            "Requesting aircraft states from OpenSky: %s",
            OPENSKY_STATES_ENDPOINT,
        )

        response = self.session.get(
            OPENSKY_STATES_ENDPOINT,
            params=params,
            timeout=HTTP_TIMEOUT_SECONDS,
        )

        response.raise_for_status()

        data = response.json()

        logger.debug(
            "OpenSky response received successfully."
        )

        return data

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()