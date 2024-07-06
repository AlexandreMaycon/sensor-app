import unittest
from App.Services import AuthService

class TestGenerateToken(unittest.TestCase):
    body = {
        'login': 'alexandre.maycon',
        'password': 'password'
    }
    AuthService.generate_token(body)
    
if __name__ == '__main__':
    unittest.main()