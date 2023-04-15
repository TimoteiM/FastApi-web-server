import jwt
import os
from datetime import datetime, timedelta

print(dir(jwt))
SECRET_KEY = str(os.environ.get('SECRET_KEY'))

ALGORITHM = os.environ.get('algorithm')


def generate_token(user_id):
    
        expiration = datetime.utcnow() + timedelta(hours=24) 
        payload = {
            'exp': expiration,
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        
        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
        return token
    
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    
    except jwt.ExpiredSignatureError:
        return 'Token has expired'
    
    except jwt.InvalidTokenError:
        return 'Invalid token'

user_id = "asdkwo234dsl"

token = generate_token(user_id)
verified_token = verify_token(token)
print(verified_token)
