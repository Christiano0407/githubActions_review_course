from fastapi.testclient import TestClient
from ..backend.api_backend.app import app, fake_db, Item, HTTPException
import pytest

# ==== TestClient | prove endpoints not use server (uvicorn) ==== #
client = TestClient(app)

# ==== Test Endpoint Root (/) ==== #