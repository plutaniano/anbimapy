import pytest

from anbimapy.anbima import Anbima


@pytest.fixture(scope="session")
def anbima():
    client = Anbima("a", "b")
    client.autenticar()
    return client
