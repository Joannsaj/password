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




























































# def create_contact(fname,lname,phone,email):
#     '''
#     Function to create a new contact
#     '''
#     new_contact = Contact(fname,lname,phone,email)
#     return new_contact

# def save_contacts(contact):
#     '''
#     Function to save contact
#     '''
#     contact.save_contact()

# def del_contact(contact):
#     '''
#     Function to delete a contact
#     '''
#     contact.delete_contact()

# def find_contact(number):
#     '''
#     Function that finds a contact by number and returns the contact
#     '''
#     return Contact.find_by_number(number)

# def check_existing_contacts(number):
#     '''
#     Function that check if a contact exists with that number and return a Boolean
#     '''
#     return Contact.contact_exist(number)

# def display_contacts():
#     '''
#     Function that returns all the saved contacts
#     '''
#     return Contact.display_contacts()
