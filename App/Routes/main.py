from fastapi import FastAPI, UploadFile, File, Depends
from App.Services import SensorService, UserService, AuthService
from App.Lib.Types import SaveEquipmentBody, SaveUserBody, Response, GenerateTokenBody
from App.Data import verify_token

app = FastAPI(
    title="SensorApp",
)

@app.get("/", tags=["Health API"])
async def heath_check():
    return {"status": "success"}

@app.post("/create-user", tags=["User"])
async def create_user(data: SaveUserBody) -> Response:
    resp = UserService.create_user(data)
    return resp

@app.post("/token", tags=["Auth"])
async def generate_token(data: GenerateTokenBody) -> dict:
    resp = AuthService.generate_token(data)
    return resp

@app.post("/save", tags=["Sensor"])
async def save_sensor(data: SaveEquipmentBody, token: str = Depends(verify_token)) -> Response:
    resp = SensorService.save(data)
    return resp

@app.post("/upload-file", tags=["Sensor"])
async def upload_csv(file: UploadFile = File(...), token: str = Depends(verify_token)) -> Response:
    resp = SensorService.save_file(file)
    return resp
