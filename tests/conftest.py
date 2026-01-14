import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
