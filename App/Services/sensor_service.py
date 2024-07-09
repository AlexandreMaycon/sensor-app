from App.Repository import Equipments
from fastapi import UploadFile
import pandas as pd
from App.Lib.Types import SaveEquipmentBody
from App.Lib.Treatment import format_date_to_compare
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import base64

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
            "message": "Equipment successfully created"
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
            "message": "Equipment successfully created"
        }
    
    def get_average(period: str):
        now = datetime.now()
        
        match period:
            case '24h':
                start_time = now - timedelta(hours=24)
            case '48h':
                start_time = now - timedelta(hours=48)
            case '1w':
                start_time = now - timedelta(weeks=1)
            case '1m':
                start_time = now - timedelta(days=30)
            case _:
                return {"error": "Invalid period"}
            
        formated_date = format_date_to_compare(start_time)
        
        data = Equipments.get_by_date(formated_date)
        if not data:
            return {"message": "No data available for the specified period"}
        
        equipment_data = {}
        
        for record in data:
            if record['equipmentId'] not in equipment_data:
                equipment_data[record['equipmentId']] = []
            equipment_data[record['equipmentId']].append(record['value'])
        
        averages = {equipmentId: sum(values) / len(values) for equipmentId, values in equipment_data.items()}
        
        plt.figure(figsize=(10, 6))
        plt.bar(averages.keys(), averages.values(), color='blue')
        plt.xlabel('Equipment ID')
        plt.ylabel('Value')
        plt.title(f'Average Sensor Values over {period}')
        plt.xticks(rotation=45)
        plt.tight_layout()

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()
        
        return {
            "status": "success",
            "plot_url": plot_url,
            "averages": averages
        }