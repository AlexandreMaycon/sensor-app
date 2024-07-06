from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("login")
        if login is None:
            raise raise_exception("Could not validate credentials")
        
    except jwt.ExpiredSignatureError:
        raise raise_exception("Token has expired")
    
    except jwt.InvalidTokenError:
        raise raise_exception("Invalid token")
    
def raise_exception(message: str) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"},
    )