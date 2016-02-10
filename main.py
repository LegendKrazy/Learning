
def main_menu():
    business_name = input("Name your company")
    print("Congratulations! You are the new CEO of " + business_name + ". Good luck in your journey!")
    print("The difficulty you choose will decide how much money you start with.")
    difficulty_select()

def inventory(item):
    inventory.append(item)

def difficulty_select():
    difficulty_level = input("Easy, Medium, Hard, or Cheat?")
    if difficulty_level == "Easy":
        interface_screen(100000)
    elif difficulty_level == "Medium":
        interface_screen(50000)
    elif difficulty_level == "Hard":
        print("You asked for it!")
        interface_screen(0)
    elif difficulty_level == "Cheat":
        interface_screen(1000000)
    else:
        print("You did not select a proper difficulty level.")
        difficulty_select()

def interface_screen(amt):
    cash = 50000 + amt
    print("Your starting cash amount is: $", cash)


main_menu()
