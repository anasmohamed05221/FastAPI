from .utils import *
from ..routers.users import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_get_user(test_user):
    response = client.get("/users/")
    assert response.status_code == status.HTTP_200_OK

    assert response.json()["email"] == "testuser@email.com"
    assert response.json()["username"] == "testuser"
    assert response.json()["first_name"] == "Test"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "2 (222) 222-2222"



def test_change_password_success(test_user):
    response = client.put("/users/password", json={"password": "test1234",
                                                   "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put("/users/password", json={"password": "test1234567",
                                                   "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Old password is incorrect."}

def test_change_phone_number_success(test_user):
    response = client.put("/users/phonenumber/3 (333) 333-3333")
    assert response.status_code == status.HTTP_204_NO_CONTENT






