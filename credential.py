

class Credential:
    """"
    A class that generates new instances of credentials
    """
    credential_list=[]

def __init__(self, account, password):

        '''
        __init__method that helps us with the properties of the users as our objects
    
        Args:
             account: new credential account
             password: new credential password

        '''
        self.account = account
        self.password = password

def save_credential(self):
        '''
        save_credential method saves credential objects into user_list
        '''
        Credential.credential_list.append(self)
