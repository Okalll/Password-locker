import unittest

from user import User
# from socialAccounts import user

class TestUser(unittest.TestCase):
    # setup and class creation up here
    def setUp(self):
        '''
        Function to help create user a/c details before each test
        '''
        self.new_user = User("Okall", "1234", "vivieokall@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Okall")
        self.assertEqual(self.new_user.password,"1234")
        self.assertEqual(self.new_user.email,"vivieokall@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)



if __name__ == '__main__':
    unittest.main()