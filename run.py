from user import User
from credential import Credential
import random

def create_user(account,password):
    """
    Function to create a new users
    """
    new_user= Credential (account,password)
    return new_user


