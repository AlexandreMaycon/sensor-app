import unittest
from App.Services import AuthService
from App.Services import UserService
from App.Lib.Types import GenerateTokenBody, SaveUserBody

class TestGenerateToken(unittest.TestCase):
    def test_generate_token(self):
        self.create_user()
        
        body = GenerateTokenBody(
            login='alexandre.maycon',
            password='password'   
        )
        
        resp = AuthService.generate_token(body)
        
        self.assertIsNotNone(resp)
    
    def create_user(self):
        body = SaveUserBody(
            name='Alexandre',
            login='alexandre.maycon',
            password='password',
        )
        
        UserService.create_user(body)
    
if __name__ == '__main__':
    unittest.main()