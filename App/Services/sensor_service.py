from App.Repository import Equipments
from fastapi import UploadFile
import pandas as pd
from App.Lib.Types import SaveEquipmentBody

class SensorService:
    
    def save(body: SaveEquipmentBody):
        repo = Equipments
        repo.create_equipment_data(
            body.equipmentId,
            body.timestamp,
            body.value
        )
        
        return {
            "status": "success",
            "message": "Equipamento criado com sucesso"
        }
    
    def save_file(file: UploadFile):
        df = pd.read_csv(file.file, sep=';')
        repo = Equipments
        
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
        