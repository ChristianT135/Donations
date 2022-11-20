def login(database, username, password):
    for user in database:
        if user == username:
            if database[user] == password:
                print("Welcome back", username, "\n")
                return username
            else:
                print("Incorrect password for", username, "\n")
                return ""
    print("User not found.  Please register. \n")
    return ""

def register(database, username):
    # could i also so  database.has_key(username):? idk 
    if username in database:
        print("Username already registered. \n")
        return ""
    else:
        print("Username has been registered. \n")
        return username