"""Module to configure pytests"""
import pytest

# local imports
from app import app


@pytest.fixture
def client():
    """App's test client"""
    return app.test_client()
