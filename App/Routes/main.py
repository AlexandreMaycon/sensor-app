from fastapi import FastAPI, UploadFile, File, Depends, Form
from App.Services import SensorService, UserService, AuthService
from App.Lib.Types\
    import SaveEquipmentBody, SaveUserBody, DefaultResponse, GenerateTokenBody, TokenResponse, AverageResponse
from App.Data import verify_token
from fastapi.templating import Jinja2Templates
import os
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SensorApp",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

templates = Jinja2Templates(directory=os.path.join("App", "Templates"))

@app.post("/create-user", tags=["User"])
async def create_user(data: SaveUserBody) -> DefaultResponse:
    resp = UserService.create_user(data)
    return resp

@app.post("/token", tags=["Auth"])
async def generate_token(username: Annotated[str, Form()], password: Annotated[str, Form()]) -> TokenResponse:
    data = GenerateTokenBody(
        login=username,
        password=password
    )
    resp = AuthService.generate_token(data)
    return resp

@app.post("/save", tags=["Sensor"])
async def save_sensor(data: SaveEquipmentBody, token: str = Depends(verify_token)) -> DefaultResponse:
    resp = SensorService.save(data)
    return resp

@app.post("/upload-file", tags=["Sensor"])
async def upload_csv(file: UploadFile = File(...), token: str = Depends(verify_token)) -> DefaultResponse:
    resp = SensorService.save_file(file)
    return resp

@app.get("/average/")
async def average(period: str | None = None):
    resp = SensorService.get_average(period)
    return resp