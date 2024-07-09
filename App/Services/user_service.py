from App.Lib.Types import SaveUserBody
from App.Repository import Users
import hashlib

class UserService:
    
    def create_user(body: SaveUserBody):
        password = body.password
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        
        repo = Users
        repo.create_user(
            body.name,
            body.login,
            password_hash
        )
        
        return {
            "status": "success",
            "message": "User successfully created"
        }