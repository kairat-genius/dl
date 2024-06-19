import jwt
from datetime import datetime


def create_token(email):

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    token_data = {email: current_time}
    secret = "ppp"

    token = jwt.encode(token_data, key=secret, algorithm='HS256')

    return token


