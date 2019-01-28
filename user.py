class User:
    """
    class that generates new instances of user accounts
    """
 
    user_list = [] #empty Users list

    def __init__(self,username,password,email):
        '''
        defining structure of the user object
        '''

        self.username =username
        self.password = password
        self.email = email