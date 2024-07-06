import unittest
from App.Lib.Types import SaveEquipmentBody
from pydantic import ValidationError

class TestErrorBodyEquipment(unittest.TestCase):
    def test_save_sensor_error(self):
        with self.assertRaises(ValidationError) as context:
            SaveEquipmentBody(
                timestamp="2023-02-15T01:30:00.000-05:00",
                value=78.42
            )
        
        errors = context.exception.errors()
        self.assertEqual(errors[0]['loc'], ('equipmentId',))
        self.assertEqual(errors[0]['msg'], 'Field required')

if __name__ == '__main__':
    unittest.main()