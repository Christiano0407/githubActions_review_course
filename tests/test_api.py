from fastapi.testclient import TestClient
from backend.api_backend.app import app, fake_db, Item, HTTPException
import pytest

# ================================================================= #
# === TestClient | prove endpoints not use server (uvicorn) === #
# ================================================================= # 
client = TestClient(app)

# =========================================================================== #
# Optional: Test with pytest fixture to clean the Database (fake_db) 
# =========================================================================== #
@pytest.fixture(name="clean_fake_db")
def fixture_clean_fake_db(): 
  """
    'Fixture' with Pytest to clean and reset the Database (fake_db) before each test
  """
  original_database = list(fake_db)
  yield # This is where execute the Test 
  fake_db[:] = original_database

# ==== Test Endpoint Root (/) ==== #
def test_read_root(): 
  """ 
    Test Endpoint To Root (/) | Come status 200 ok | return message: New API Application
  """
  # get & Affirm the response from the root endpoint # 
  response = client.get("/") 
  # Affirm the response in the endpoint root is 200 ok #
  assert response.status_code == 200
  # get the json response from the root endpoint (get) #
  expected_message = {"message": "Welcome to my New API Application With FastAPI"}
  assert response.json() == expected_message

## ==== Test To Get all Items (/items/) ==== ##
def test_read_items(clean_fake_db): 
  """
    Test to get all Items (/items/) from database (fake_db) | return status code 200 ok
  """
  # Affirm the response from endpoint (get) #
  response = client.get("/items/")
  ## Response status code 200 ok ##
  assert response.status_code == 200
  ### Verify the response is the type list ###
  assert isinstance(response.json(), list)
  ### Verify the response is equal to fake_db (len) ###
  assert len(response.json()) == len(fake_db)
  #### Verify Json Response Data (simulated) is equal to fake_db ####
  assert response.json() == fake_db

### ==== Test To Get Items By ID (/items/{item_id}) | Error 404 ==== ### 
def test_read_item(clean_fake_db):
  """
    Verify if the endpoint return 'ID' (exist), and the status code 200
  """
  existing_item_id = 1
  response = client.get(f"/items/{existing_item_id}")
  assert response.status_code == 200
  expected_item = next((item  for item in fake_db if item["id"] == existing_item_id), None)
  assert response.json() == expected_item

def test_read_item_not_exist():
  """
    Verify if return a Error 404 if not exist the item with ID
  """
  non_exist_item_id = 999
  response = client.get(f"/items/{non_exist_item_id}")
  assert response.status_code == 404
  assert response.json() == {"detail": "Item Not Exist."}