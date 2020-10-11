class User:
    '''
    Class that generates new instances of users.
    '''

    user_list = [] #empty user list
    def __init__(self,username,password):

        self.username = username
        self.password = password


    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)    


    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)   


    @classmethod
    def authentic(cls):

        for user in cls.user_list:
            if user.username == username & user.password == password:
                return user