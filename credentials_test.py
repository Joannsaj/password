import unittest # Importing the unittest module
from credentials import Credentials # Importing the user class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter","joan","9waszxer") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"Twitter")
        self.assertEqual(self.new_credentials.username,"joan")
        self.assertEqual(self.new_credentials.password,"9waszxer")

    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []


    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Gmail","user","zxcvbnml") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)    


    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Gmail","user","zxcvbnml") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credentials object
            self.assertEqual(len(Credentials.credentials_list),1)

    
    def test_find_credentials_by_account(self):
        '''
        test to check if we can find a credentials by phone account and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Gmail","user","zxcvbnml") # new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account("Gmail")

        self.assertEqual(found_credentials.username,test_credentials.username)


    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

        
if __name__ == '__main__':
    unittest.main()        