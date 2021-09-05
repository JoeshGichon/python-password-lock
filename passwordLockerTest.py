from passwordLoker import User,Credentials
import unittest 

class TestPassword(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User("Joesh Gichon","JG","5678")
        self.new_credentials = Credentials("facebook","JG","5678")
