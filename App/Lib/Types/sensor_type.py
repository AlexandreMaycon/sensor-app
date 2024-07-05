from typing_extensions import TypedDict

class BodyRequest(TypedDict):
    equipmentId: str
    timestamp: str
    value: float
    
class Response(TypedDict):
    status: str
    message: str
