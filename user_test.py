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
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user test checks to test if the user can save multiple users to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Okall", "1234", "vivieokall@gmail.com") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_confirm_user(self):
        '''
        Function to confirm login details to current user
        '''
        self.new_user = User("Okall", "1234", "vivieokall@gmail.com")
        self.new_user.save_user()
        test_user= User("Okall", "1234", "vivieokall@gmail.com")
        test_user.save_user()
        active_user = User.confirm_user("Okall", "1234", "vivieokall@gmail.com")
        self.assertTrue(active_user)

    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_user(),User
        .user_list)

if __name__ == '__main__':
    unittest.main()