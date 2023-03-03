import json

class Plant:
    file = "database/plants.json"


    def __init__(self, name, address):
        self.name = name
        self.address = address

    def generate_dict(self):
        return {
            "name": self.name,
            "address": self.address
        }

    def save(self):
        file = open(self.file, "r")
        plants = json.loads(file.read())
        file.close()
        file = open(self.file, "w")
        plant = self.generate_dict()
        if len(plants) > 1:
            plant["id"] = len(plants) + 1
        else:
            plant["id"] = 1
        plants.append(plant)
        file.write(json.dumps(plants))
        file.close()

    @classmethod
    def get_all_plants(cls):
        file = open(cls.file, "r")
        plants = json.loads(file.read())
        file.close()
        for plant in plants:
            print(plant["name"])
            print(plant["address"])


class Employee:
    file = "database/employees.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id

    def generate_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "plant_id":self.plant_id
        }

    def save(self):
        file = open(self.file, "r")
        employees = json.loads(file.read())
        file.close()
        file = open(self.file, "w")
        employee = self.generate_dict()
        if len(employees) > 1:
            employee["id"] = len(employees) + 1
        else:
            employee["id"] = 1
        employees.append(employee)
        file.write(json.dumps(employees))
        file.close()

    @classmethod
    def get_all_employees(cls):
        file = open(cls.file, "r")
        employees = json.loads(file.read())
        file.close()
        for employee in employees:
            print(employee["name"])
            print(employee["email"])
            print(employee["plant_id"])


#def check_email(email):
#   match = re.search(r'[\w.-]+@[\w.-]+', email)
#   if match:
#        return True
#   else:
#        return False
