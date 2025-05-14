# Create class
class User:
    pass

# Create object
user_1 = User()
user_2 = User()

# Create attribute
user_1.id = "001"
user_1.username = "alice"
print(user_1.username)

user_2.id = "002"
user_2.username = "jack"
print(user_2.username)

#####################################################################################
# Class Constructor
class User:
    # __init__ is used to initialize objects of a class.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "alice")
user_2 = User("002", "jack")

# Call Method: user_1 decided to follow user_2
user_1.follow(user_2)
print(user_1.followers)     # 0
print( user_1.following)    # 1
print(user_2.followers)     # 1
print( user_2.following)    # 0