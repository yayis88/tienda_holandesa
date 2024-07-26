import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def validate_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_jwt if decoded_jwt["exp"] >= datetime.utcnow() else None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None