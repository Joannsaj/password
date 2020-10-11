class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] #empty user list
    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password


    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)


    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self) 


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list    