# import pyperclip
import random
from user import User

def create_user_accounts(username,password,email):
    '''
    to allow us create users to login and use the system
    :param your_name:
    :param your_password:
    :param your_email:
    :return:
    '''
    new_user_account = User(username,password,email)
    return new_user_account

def save_user_account(user_account):
    '''
    allows us to save the system users once they create their logins
    :param user_account:
    :return:
    '''
    User.save_user_account(user_account)


def user_authentication(username,password,email):
    '''
    to check user logins and log the user to the system
    :param your_name:
    :param your_password:
    :param your_email:
    :return:
    '''
    confirm_app_user = User.confirm_app_user(username,password,email)
    return confirm_app_user

def generate_acc_password():
    '''
    automatically generate the user password
    :return:
    '''
    auto_password = User.generate_acc_password()
    return auto_password

def display_user_accounts():
    """
    To view all system users that have been saved
    """
    return User.display_user_accounts()


def create_user_account(account, username, password):
    '''
    function to create a new user details
    '''
    new_user_account = User(account, username, password)
    return new_user_account

def save_user_accounts(user_account):
    '''
    function to save user account5
    '''
    user_account.save_user_account()

def delete_users_account(user_account):
    '''
    function to delete a user account
    :param user_account:
    :return:
    '''
    user_account.delete_user_account()

def find_user_account(user_account):
    '''
    finding a user account and return its details
    :param user_account:
    :return:
    '''
    return User.find_account_by_name(user_account)

def check_existing_accounts(user_account):
    '''
    function that checks if  userAccount exists and returns a boolean
    :param user_account:
    :return:
    '''
    return User.user_account_exists(user_account)

def display_all_user_accounts():
    '''
    function to display all stored userAccount
    :return:
    '''
    return User.display_user_accounts()

def main():

    print(' ')
    print('Hello, Welcome to safe account!')
    while True:
        print(' ')
        print("-"*70)
        print('Use these codes to navigate: \n ca-Create a new Safe Account \n li-Log Into Safe account to access your logins \n ex-Exit')
        short_code = input('Enter an option: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*70)
            print(' ')
            print('To create a new safelock account:')
            account_name = input('Enter your name.. ').strip()
            account_password = input('Enter your password..').strip()
            save_user_account(create_user_accounts(account_name,account_password))
            print(" ")
            print(f'New safe account created for: {account_name} ')
            elif short_code == 'li':
              print("-"*70)
            print(' ')
            print('To login, enter your safe account details:')
            account = input('Enter your account name: ').strip()
            password = str(input('Enter your password: '))
            print("\n Your Password is..")
            validation = ''
            chars = "abcdefghijklmnopqrstuvwxyz1234567890!#.,?"
            validation = ''.join(random.choice(chars)for _ in range(10))
            user_exists = user_authentication(account,password)
            if user_exists == account:
                print(" ")
                print(f'Welcome {account}. Please choose an option to continue.')
                print(' ')
                while True:
                    print("Use these short codes : \n cl : create new logins, dl : display saved logins, sl : search for a login, ex : exit the Safelock app ")
                    short_code = input().lower()
                    if short_code=='ex':
                        print(" ")
                        print(f"Thank you for using Safe {account}")
                        break
                    elif short_code == 'cl':
                        print("New user Media Logins")
                        print("="*40)
                        print ("Account name e.g twitter,instagram,facebook")
                        user_acc = input()
                        print("Account username ...")
                        acc_username = input()
                        while True:
                            print(' ')
                            print("-" * 70)
                            print(
                                'Please choose an option for entering a password: \n ep-enter existing password \n gp-auto-generate password \n ex-exit')
                            password_options = input('Enter an option: ').lower().strip()
                            print("-" * 70)
                            if password_options == 'ep':
                                print(" ")
                                user_account_password = input('Enter your password: ').strip()
                                break
                            elif password_options == 'gp':
                                userAccount_password = generate_acc_password()
                                break
                            elif password_options == 'ex':
                                break
                            else:
                                print('Sorry! Enter given codes.')
                        save_user_Account(create_user_Account(user_acc,acc_username,user_account_password)) # create and save new contact.
                        print ('\n')
                        print(f" {user_acc} Profile created")
                        print ('\n')

                    elif short_code == 'sl':
                        print("Enter the user account type you want to search for  facebook")
                        search_account = input()
                        if check_existing_accounts(search_account):
                            search_user_account = find_user_account(search_account)
                        print(f"{search_user_account.user_account} {search_user_account.user_account_username}")
                        print('-' * 20)
                        print(f"Account: {search_user_account.user_account}")
                        print(f"Username: {search_user_account.user_account_username}")
                    elif short_code == 'dl':
                        if display_all_user_accounts():
                            print("Here is a list of all your saved logins")
                        print('\n')
                        for user_accounts in display_all_user_accounts():
                                print(f"Account: {User.user}, Username:{User.user_Account_username}, Password: {user_Acount.user_Account_password}")
                        print('\n')
                    else:
                        print('\n')
                        print("No saved social media logins yet")
                        print('\n')

                   else:
                        print("That account media account does not exist")
                        print(' ')
                   else:
                        print('Sorry! Use provided short codes and try again.')

                   else:
                        print('')
                        print('Sorry! Use provided short codes and try again or Create an Account.')

if __name__ == '__main__':
    main()