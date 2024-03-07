from jose import jwt


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

class Token():
    def create_access_token(data: dict):
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    def decode(token):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

