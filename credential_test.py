import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        set up method to run before  each test cases
        """
        self.new_credential= Credential("Okall", "1234", "vivieokall@gmail.com")