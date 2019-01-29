from user import User
from credential import Credential
import random

def create_user(account,password):
    """
    Function to create a new user
    """
    new_user= Credential (account,password)
    return new_user


def save_user():
    """
    saving the user
    """
    User.save_user

def display_user():
    return User.display_users()

def save_credential(self):
            '''
            save_credential method saves credential objects into credential_list
            '''
            Credential.credential_list.append(self)

def confirm_user(cls, username, password, email):
        '''
        Method that checks if the name, password and email entered match entries in the users_list
        '''
        current_user = ''
        for user in User.user_list:
            if (user.username == username and user.password == password):
                current_user = user.username
        return current_user

def main():
        print(' ')
        print('Hello Welcome to password-locker')
        while True:
            print(' ')
            print("-"*10)
            print('try out this: \n ca \n li \n ex')
            short_code = input('choose any of the above: ').lower().strip()
            if short_code == 'ex':
                break

            elif short_code == 'ca':
                print("-"*10)
                print(' ')
                print('create new account:')

                print("username")
                username = input()

                print("password")
                password = input()

                print("email")
                email = input()

                save_user(create_user(username,password,email))
                #creates and saves new user
                print ('\n')
                print(f"New User {username} {email} created")