import pytest
from EmployeeApi import XClientsAPI

BASE_URL = "https://x-clients-be.onrender.com"
USERNAME = "raphael"
PASSWORD = "cool-but-crude"


@pytest.fixture(scope="session")
def api():
    return XClientsAPI(BASE_URL, USERNAME, PASSWORD)
