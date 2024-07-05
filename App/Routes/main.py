from fastapi import FastAPI, UploadFile, File
from App.Services import SensorService
from App.Lib.Types import BodyRequest
from App.Lib.Types import Response

app = FastAPI(
    title="SensorApp",
)

@app.get("/")
async def heath_check():
    return {"status": "success"}

@app.post("/save", tags=["Sensor"])
async def save_sensor(data: BodyRequest) -> Response:
    resp = SensorService.save(data)
    return resp

@app.post("/upload-file", tags=["Sensor"])
async def upload_csv(file: UploadFile = File(...)) -> Response:
    resp = SensorService.save_file(file)
    return resp
