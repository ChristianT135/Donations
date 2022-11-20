from donations_pkg.homepage import show_homepage
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations
from donations_pkg.user import login
from donations_pkg.user import register



database = { "admin" : "password123", "password123" : "admin", "user" : "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print(f"You are logged in as {authorized_user}")

    
    option = input("Choose an option:")
    print()
    
    if option == "1":
        username = input("Enter user name: "). lower()
        password = input("Enter user password: ")
        print()
        authorized_user = login(database, username, password)
    
    elif option == "2":
        username = input("Enter user name: ").lower()
        password = input("Enter user password: ")
        print()
        authorized_user = register(database, username)
        if authorized_user:
            database[username] = password
            
    elif option == "3":
        if authorized_user:
            print("Your not logged in")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            
    elif option == "4":
        show_donations(donations)
        
    elif option == "5":
        print("leaving DonateMe .....\n")
        quit()
    
        

