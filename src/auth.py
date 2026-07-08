import os
import jwt
import datetime

SECRET_KEY = os.getenv("JWT_SECRET", "development-secret")


def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"


def main():
    username = input("Enter username: ")

    token = generate_token(username)

    print("\nGenerated Token:\n")
    print(token)

    print("\nDecoded Payload:\n")
    print(verify_token(token))


if __name__ == "__main__":
    main()
