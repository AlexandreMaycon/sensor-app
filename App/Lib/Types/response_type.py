from pydantic import BaseModel

class DefaultResponse(BaseModel):
    status: str
    message: str

class TokenResponse(BaseModel):
    status: str
    access_token: str
    token_type: str
    
class AverageResponse(BaseModel):
    status: str
    plot_url: str
    averages: dict