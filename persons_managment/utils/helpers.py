import json


def create_file():
    f = open("database/persons.json", "w")
    f.write("[]")
    f.close()


def get_all_humans():
    try:
        f = open("database/persons.json", "r")
    except FileNotFoundError:
        if os.path.exists("database"):
            create_file()
        else:
            os.mkdir("database")
            ceate_file()
        file = open("database/persons.json", "r")
    data = json.loads(file.read())
    file.close()
    return data


def write_new_human(human):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
        human["id"] = len(data) + 1
    data.append(human)
    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()

def unique_email(email):
    data = get_all_humans()
    for el in data:
        if el["email"] == email:
            return False
    return True

def edit_info(id):
    data = get_all_humans()
    for el in data:
        if el["id"] == id:
            el["first_name"] = input("Enter new first name: ")
            el["last_name"] = input("Enter new last name: ")
            el["email"] = input("Enter new email: ")

    file = open("database/persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()