from models import Plant, Employee
from validate_email import validate_email

while True:
    print("1. Add Plant.\n2. Get all plants.\n3. Add Employee\n4. Get all employees")
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plants name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        Plant.get_all_plants()
    elif flag == 3:
        name = input("Employee name:")
        email = input("Employee email:")
        #if email.count("@") == 1 and email[0] != "@" and email.count(".") > 0:
            #pass
        is_valid = validate_email(email)
        if is_valid:
            pass
        else:
            print("Wrong email!")
            email = input("Employee email:")
        plant_id = int(input("Plant id"))
        employee = Employee(name, email, plant_id)
        employee.save()
    elif flag == 4:
        Employee.get_all_employees()
    else:
        print("Wrong choise!")


