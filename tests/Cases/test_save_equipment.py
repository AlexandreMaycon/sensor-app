import unittest
from App.Services import SensorService
from App.Lib.Types import SaveEquipmentBody

class TestSensor(unittest.TestCase):
    def test_save_sensor_success(self):
        body = SaveEquipmentBody(
            equipmentId="EQ-12495",
            timestamp="2023-02-15T01:30:00.000-05:00",
            value=78.42
        )
        
        resp = SensorService.save(body)

        self.assertIsNotNone(resp)

if __name__ == '__main__':
    unittest.main()