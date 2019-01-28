class Credential:
    """"
    A class that generates new instances of credentials
    """
    credential_list=[]

    def __init__(self, username, password, email):

        '''
        __init__method that helps us with the properties of the users as our objects
    
        Args:
             username: new credential account
             password: new credential password
             email: new credential email address

        '''
        self.username = username
        self.password = password
        self.email = email