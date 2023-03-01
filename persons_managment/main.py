from utils.helpers import *

while True:
    print("1. Add new person! \n2. Get all persons!)\n3. Edit personal data.")
    try:
        flag = int(input("Choose  what you want to do: "))
    except ValueError:
        print ("There is no such choice.")
    if flag == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")

        if "@" and ".com" not in email:
            print("Wrong email address")

        while not unique_email(email):
            print("This email already registered!")
            email = input("Email: ")

        human = {"first_name": first_name, "last_name": last_name, "email": email}
        write_new_human(human)

    elif flag == 2:
        humans = get_all_humans()
        for human in humans:
            print(human["first_name"])
            print(human["last_name"])
            print(human["email"])
            print("=======================================")

    elif flag == 3:
        try:
            id = int(input("Enter your id: "))
        except ValueError:
            print ("It's not an id!")
        edit_info(id)

    else:
        print("Wrong menu item!")
