class User:
    """
    class that generates new instances of users
    """
    user_list = []  # empty Users list

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    

    def __init__(self, username, password, email):
        '''
        defining structure of the user object
        '''

        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def confirm_user(cls, username, password, email):
        '''
        Method that checks if the name, password and email entered match entries in the users_list
        '''
        current_user = ''
        for user in User.user_list:
            if (user.username == username and user.password == password):
                current_user = user.username
        return current_user

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list
