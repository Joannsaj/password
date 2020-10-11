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
    contact.save_credentials()

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
    return Contact.display_credentials()
