class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] #empty user list
    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password