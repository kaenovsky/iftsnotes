# Encapsulation in Python (OOP)
# https://www.codecademy.com/courses/python-for-programmers/articles/encapsulation-python

class UserInfo:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

    """
    Class Methods
    
    A class can also contain methods that can be accessed by 
    objects of the class. The example below shows the class 
    UserInfo with the method check_username that checks whether 
    a username is saved in the object or not. 
    """

    def check_username(self, username_to_check):
        if username_to_check == self.username:
            return True
        else:
            return False

user = UserInfo('jake', 'jake_fake@duck.com')

print(user.email_address)
print(user.username)

# check for the username [true & false]

print(user.check_username('kate')) # false
print(user.check_username('jake')) # true