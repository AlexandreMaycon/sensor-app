from App.Repository import Equipaments
from fastapi import UploadFile, HTTPException
import pandas as pd

class SensorService:
    
    def save(data: dict):
        if "equipmentId" not in data or "timestamp" not in data or "value" not in data:
            raise HTTPException(status_code=400, detail="Dados inválidos")
        
        repo = Equipaments
        repo.create_equipment_data(
            data["equipmentId"],
            data["timestamp"],
            data["value"]
        )
        
        return {
            "status": "success",
            "message": "Equipamento criado com sucesso"
        }
    
    def save_file(file: UploadFile):
        df = pd.read_csv(file.file, sep=';')
        repo = Equipaments
        
        for _, row in df.iterrows():
            repo.create_equipment_data(
                row['equipmentId'],
                row['timestamp'],
                row['value']
            )
        
        return {
            "status": "success",
            "message": "Equipamento criado com sucesso"
        }
        