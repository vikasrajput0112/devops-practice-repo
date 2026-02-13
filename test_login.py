# Basic test cases for login module

from login import login

def test_valid_login():
    result = login("admin", "1234")
    assert result == "Login Successful"
    print("Test valid login: PASSED")

def test_invalid_login():
    result = login("user", "wrong")
    assert result == "Invalid Credentials"
    print("Test invalid login: PASSED")

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
