import os
import jwt

from auth import generate_token, verify_token


def test_generate_and_verify_token():
    token = generate_token("Aaron")

    decoded = verify_token(token)

    assert decoded["username"] == "Aaron"


def test_generate_token_returns_string():
    token = generate_token("Aaron")

    assert isinstance(token, str)


def test_invalid_token():
    result = verify_token("this.is.not.valid")

    assert result == "Invalid token"


def test_expired_token():

    expired = jwt.encode(
        {
            "username": "Aaron",
            "exp": 1
        },
        os.getenv("JWT_SECRET", "development-secret"),
        algorithm="HS256"
    )

    result = verify_token(expired)

    assert result == "Token expired"
