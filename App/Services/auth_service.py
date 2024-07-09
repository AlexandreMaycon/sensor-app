from App.Repository import Users
from fastapi import HTTPException, status
from App.Lib.Types import GenerateTokenBody
from datetime import datetime, timedelta, timezone
import hashlib
import jwt

class AuthService:
    
    def generate_token(body: GenerateTokenBody):
        user = Users.get_user_by_login(body.login)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        password_hash = hashlib.sha256(body.password.encode("utf-8")).hexdigest()
        if user["password"] != password_hash:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token_expires = timedelta(minutes=15)
        expire = datetime.now(timezone.utc) + access_token_expires
        
        encoded_data = {
            'login': user['login'],
            'exp': expire
        }

        encoded_jwt = jwt.encode(encoded_data, 'secret', algorithm='HS256')
        
        return {
            "status": 'success',
            "access_token": encoded_jwt,
            "token_type": "bearer",
        }