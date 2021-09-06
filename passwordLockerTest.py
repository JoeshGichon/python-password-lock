from passwordLoker import User,Credentials
import unittest 

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Joesh Gichon","JG","5678")
        self.new_credentials = Credentials("facebook","JG","5678")

    def tearDown(self):
        User.users_list = []
        Credentials.credentials_list = []
    
    def test_init(self):
        self.assertEqual(self.new_user.official_name,"Joesh Gichon")
        self.assertEqual(self.new_user.username,"mn")
        self.assertEqual(self.new_user.password,"5678")
        self.assertEqual(self.new_credentials.account,"facebook")
        self.assertEqual(self.new_credentials.username,"JG")
        self.assertEqual(self.new_credentials.password,"5678")

    def test_save_user(self): 
        self.new_user.save_user() 
        self.new_credentials.save_credentials()
        self.assertEqual(len(User.users_list),1) 
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self): 
        self.new_credentials.save_credentials()
        test_credential = Credentials("Instagrame","Joe","JT")
        test_credential.save_credentials()
        message = "Cannot add multiple user"
        self.assertGreater(len(Credentials.credentials_list),1,message)

    def test_save_multiple_users(self): 
        self.new_user.save_user()
        test_user = User("Joe Tech","JT","0000")
        test_user.save_user()
        
        self.assertEqual(len(User.users_list),2)

    def test_find_account_by_password(self): 
        self.new_user.save_user()
        test_user = User("Mercy Mumbi","Alice","9876")
        test_user.save_user()
        
        found_user = User.find_by_password("9876")
        
        self.assertEqual(found_user.password,test_user.password)

if __name__ == '__main__':
    unittest.main()   