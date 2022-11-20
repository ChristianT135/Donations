def show_homepage():
    print("\n       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")
 
def donate(username):
    donation_amt = float(input("Enter amount which you'll like to donate: "))
    donation= username + "donated" + str(donation_amt)
    print ("Thank you", username)
    return donation

def show_donations(donation):
    print("\n--- All Donations ---")
    if donation ==[]:
        print("Currently, there are no donations.")
    else:
        # could i use the for donation i range(len(donation)) instead of the for donation in donation * i saw on google but it wasn't working 
       # print(donation)? idk i was thinking if this could work. i have no idea lol coding is hard 
        for donation in donation:
            print(donation)