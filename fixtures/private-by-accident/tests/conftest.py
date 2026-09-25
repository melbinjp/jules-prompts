import pathlib
import urllib.request

import pytest

WEIGHTS = pathlib.Path.home() / ".cache" / "heron" / "unmix-v2.bin"
URL = "https://models.example-hub.org/unmixing/v2/weights.bin"


@pytest.fixture(scope="session")
def weights():
    """The reference model the tests compare against. Fetched on first use, cached after."""
    if not WEIGHTS.exists():
        WEIGHTS.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(URL, WEIGHTS)
    return WEIGHTS.read_bytes()
