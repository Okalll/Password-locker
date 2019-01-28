class User:
    """
    class that generates new instances of user accounts
    """
    user_list = []  # empty Users list

    def save_user(self):
        '''
        save_contact method saves user objects into user_list
        '''
        User.user_list.append(self)

    def __init__(self, username, password, email):
        '''
        defining structure of the user object
        '''

        self.username = username
        self.password = password
        self.email = email
