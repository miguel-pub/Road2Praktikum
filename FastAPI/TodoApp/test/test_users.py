from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_current_user] = override_get_current_user
app.dependency_overrides[get_db] = override_get_db
def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "mig"
    assert response.json()["email"] == "mig@mig.com"
    assert response.json()["first_name"] == "mig"
    assert response.json()["last_name"] == "mig"
    assert response.json()["phone_number"] == "1234567890"
    assert response.json()["role"] == "admin"
    

def test_change_password_success(test_user):
    response = client.put("/user/password", json={"password": "password", "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={"password": "wrongpassword", "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change"}
    
def test_change_phonenumber_success(test_user):
    response = client.put("/user/phonenumber/222222222")
    assert response.status_code == status.HTTP_204_NO_CONTENT