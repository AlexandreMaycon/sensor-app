from pydantic import BaseModel

class SaveEquipmentBody(BaseModel):
    equipmentId: str
    timestamp: str
    value: float

class SaveUserBody(BaseModel):
    name: str
    login: str
    password: str
    
class GenerateTokenBody(BaseModel):
    login: str
    password: str

class Response(BaseModel):
    status: str
    message: str
