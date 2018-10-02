# pylint: disable=missing-docstring,redefined-outer-name
import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    yield CliRunner()
