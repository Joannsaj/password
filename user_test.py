import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("heyoo","qwaszxer") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"heyoo")
        self.assertEqual(self.new_user.password,"qwaszxer")

    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("user","polkmniu") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)    


    def test_authentic(self):
        self.new_user.save_user()
        test_user = User("user","zxcvbnml") # new user
        test_user.save_user()

        find_user = User.find_by_account("user","zxcvbnml")

        self.assertEqual(found_user.username,test_user.username)
        self.assertEqual(found_user.password,test_user.password)

if __name__ == '__main__':
    unittest.main()