#!/usr/bin/env python3.8

from user import User
from credentials import Credentials
import random

def create_user(username , password):
    '''
    Function to create a new user
    '''
    new_user = User(username , password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def authentic(username ,password):
    '''
    Function that finds a user by username and password and returns the user
    '''
    return User.authentic(username ,password)

# credentials functions

def create_credentials(account, username, password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(account):
    '''
    Function that finds credentials by account and returns the credentials
    '''
    return Credentials.find_by_account(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def main():
    print("LOCKER")
    print("A secure place to store your passwords")
    print('\n')
    print("Enter your name")
    name = input()

    print(f"Hello {name}, login or sign up to use this application")
    print('\n')
    print("Use these short codes: su - To sign up, li - To login,")

    while True:
        short_code = input().lower()

        if short_code == 'su':
            print("Sign up")
            print("-"*10)

            print("Enter a username")
            username = input()

            print("Enter a password")
            password = input()

   
            save_user(create_user(username, password)) # create and save new user
            print ('\n')
            print(f"New User '{username}' created")
            print ('\n')

        elif short_code == 'li': 
            print("Enter your username")
            search_username = input()

            print("Enter your password")
            search_password = input()

            if authentic(search_username , search_password):
                search_user = authentic(search_username , search_password)
                print(f"{search_user.username} {search_user.password}")
                print('-' * 20)

            else:
                print("That user does not exist")
   
        else:
            print("Please enter a valid code")


        
        print("Use these short codes: ac - add credentials, dc - display_credentials, fa - find credentials to an account, de - delete credentials, ex - exit credentials list")

        if short_code == 'ac':
            print("New Credentials")
            print("-"*10)

            print ("Enter account eg.Gmail")
            account = input()
 
            print("Enter username")
            username = input()

            print("Enter account password")
            password = input()

            save_credentials(create_credentials(account, username, password)) 
            print ('\n')
            print(f"For {account} username '{username}' and password '{password}'.")
            print ('\n')   

        elif short_code == 'dc':

            if display_credentials():
                print("These are the credentials for your various accounts")
                print('\n')

                for credentials in display_credentials():
                    print(f"{credentials.account} ...... {credentials.username} -- {credentials.password}")

                print('\n')
            else:
                print('\n')
                print("No credentials found")
                print('\n') 


        elif short_code == 'fa':

            print("Enter the account you want to search for")

            search_account = input()
            if find_credentials(search_account):
                search_accounts = find_by_account(search_account)
                
                print('-' * 20)
                print(f"Account----{search_accounts.account}")
                print(f"Username----{search_accounts.username}")
                print(f"Password----{search_accounts.password}")
            else:
                print("That account does not exist")      


        elif short_code == "de":
            print("Enter the account of the Credentials you want to delete")
            search_account = input().
            if find_credentials(search_account):
                search_credential = find_by_account(search_account)
                search_credential.del_credentials()
                print('\n')
                print(f"{search_credential.account} has been deleted successfully")
                print('\n')
            else:
                print("That account does not exist")          

if __name__ == '__main__':

    main()        


# def main():
#     print("Hello Welcome to your contact list. What is your name?")
#     user_name = input()

#     print(f"Hello {user_name}. what would you like to do?")
#     print('\n')

#     while True:
#         print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

#         short_code = input().lower()

#         if short_code == 'cc':
#             print("New Contact")
#             print("-"*10)

#             print ("First name ....")
#             f_name = input()

#             print("Last name ...")
#             l_name = input()

#             print("Phone number ...")
#             p_number = input()

#             print("Email address ...")
#             e_address = input()


#             save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
#             print ('\n')
#             print(f"New Contact {f_name} {l_name} created")
#             print ('\n')

#         elif short_code == 'dc':

#             if display_contacts():
#                 print("Here is a list of all your contacts")
#                 print('\n')

#                 for contact in display_contacts():
#                     print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

#                 print('\n')
#             else:
#                 print('\n')
#                 print("You dont seem to have any contacts saved yet")
#                 print('\n')

#         elif short_code == 'fc':

#             print("Enter the number you want to search for")

#             search_number = input()
#             if check_existing_contacts(search_number):
#                 search_contact = find_contact(search_number)
#                 print(f"{search_contact.first_name} {search_contact.last_name}")
#                 print('-' * 20)

#                 print(f"Phone number.......{search_contact.phone_number}")
#                 print(f"Email address.......{search_contact.email}")
#             else:
#                 print("That contact does not exist")

#         elif short_code == "ex":
#             print("Bye .......")
#             break
#         else:
#             print("I really didn't get that. Please use the short codes")   

# if __name__ == '__main__':

#     main()                                    