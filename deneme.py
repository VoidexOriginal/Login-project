


trytime = 0

# import user database

import users_data

# LİMİTS

while trytime <= 5:

# get input from user
 username = input("username: ")

 password = input("password: ")


# validate user credentials
 if username in users_data.users and users_data.users[username] == password:
    print("login successful")

    break

 else:
    print("invalid username or password")

    trytime += 1