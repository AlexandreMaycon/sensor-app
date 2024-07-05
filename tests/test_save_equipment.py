import unittest
from App.Services import SensorService
from App.Lib.Types import Response
from fastapi import HTTPException

class TestSensor(unittest.TestCase):
    def test_save_sensor_success(self):
        body = {
            "equipmentId": "EQ-12495",
            "timestamp": "2023-02-15T01:30:00.000-05:00",
            "value": 78.42
        }
        
        resp = SensorService.save(body)

        self.assertIsNotNone(resp)
        
    def test_save_sensor_error(self):
        body = {
            "timestamp": "2023-02-15T01:30:00.000-05:00",
            "value": 78.42
        }

        with self.assertRaises(HTTPException) as context:
            SensorService.save(body)
        
        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "Dados inválidos")

if __name__ == '__main__':
    unittest.main()