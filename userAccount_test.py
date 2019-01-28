import unittest

from userAccounts import UserAccounts
# from socialAccounts import userAccounts

class TestUserAccounts(unittest.TestCase):
    # setup and class creation up here
    def setUp(self):
        '''
        Function to help create user a/c details before each test
        '''
        self.new_user = UserAccounts("Okall", "1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_userAccount.account_name,"Okall")
        self.assertEqual(self.new_userAccount.account_password,"1234")