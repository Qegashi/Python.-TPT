# this function removes spaces and new lines for column from right and left
from os import read, write


def strip(string):
    return string.strip()

# this function reads database from contacts.txt file


def read_database():
    file = open("contacts.txt", mode="r", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file


def write_database(db):
    file = open("contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db:
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory


def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")

def medium_age(db):
    sum = 0
    count = len(db)
    for i in range(0, len(db)):
        row = db[i]
        sum = sum+int(row[2])
    print(f"Medium age is {sum / count}")

def print_out_commands(db):
    print("Commands are:")
    print("1. list users")
    print("2. edit user")
    print("3. add user")
    print("4. remove user")
    command = input("What is your command?: ")

    if command == "1":
        print(db)

    elif command == "2":
        row = int(input("Row: "))
        column = int(input("Column: "))
        new_value = input("New value: ")
        db[row][column] = new_value
        write_database(db)

    elif command == "3":
        name = input("Write user's name: ")
        phone = input("Write user's phone: ")
        age = input("Write user's age: ")
        mail = input("Write user's mail: ")
        user = (f"\n{name}, {phone}, {age}, {mail}")
        file = open("contacts.txt", "a")
        file.write(user)
        file.close()

    elif command == "4":
        row = int(input("Row to delete: "))
        db[row] = ""
        write_database(db)

    else: print("No command was assigned to that number")
def main():
    db = read_database()
    print_out_database(db)
    medium_age(db)
    print_out_commands(db)
    


main()

