import getpass

class User:
    users_database = {}
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False

    @classmethod
    def add_user(cls, username, password):
        if username in cls.users_database:
            print("Username already exists! Try different username.")
            return False
        cls.users_database[username] = User(username, password) 
        return True
    
    @classmethod
    def authenticate_user(cls, username, password):
        user = cls.users_database.get(username)
        if user and user.password == password:
            return user
        return None
    
def register_user():
    username = input("Enter username: ")
    password = getpass.getpass("Enter a Password: ")

    if User.add_user(username, password):
        print("Successfully Register User! ")
    else:
        print("User Registration Failed! ")

def login_user():
    username = input("Enter username: ")
    password = getpass.getpass("Enter a Password: ")
    if User.authenticate_user(username, password):
        print("Login Successful!")
    else:
        print("Invalid Username or Password!")


