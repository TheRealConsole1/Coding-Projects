import random #
import os
username = input("Please Enter Your Username: ").title()
def read():
    exists = os.path.exists(f"{username} Programs.txt")
    if exists == False:
        print("Warning, File does not exist, making now")
        f = open(f"{username} Programs.txt", "x")
    else:
        print(f"Hello, {username} and welcome to your ideas page")
    f = open(f"{username} Programs.txt", "r")
    print("Here is the full list of Program Ideas, happy thinking!")
    content = (f.read())
    print(content)
    f = f.close()
    return
def write():
    f = open(f"{username} Programs.txt", "a")
    print("Checking File Size")
    size = os.path.getsize(f"{username} Programs.txt") 
    if size == 0:
        add = input("File Size is 0, adding new entry. What would you like to add?: ")
        new_add = add + (", ")
        new_add = f.write(new_add)
        f.close()
        return
    if size > 0:
        print("There is already an entry in here, adding another")
        add = input("What would you like to add?: ")
        new_add = add + (", ")
        new_add = f.write(new_add)
        f.close()
        return
def delete():
    with open(f'{username} Programs.txt', "r") as f:
        content =f.read()
        ideas_list = content.split(", ")
        target = input("What would you like to delete: ")
        filtered_ideas = [item for item in ideas_list if item != target]
        with open(f"{username} Programs.txt", "w") as f:
            new_content = ", ".join(filtered_ideas)
            f.write(new_content)
        print(f"{target} has been removed.")
def ra():
    with open(f"{username} Programs.txt", "r") as f:
        content = f.read().split(", ")
        choice = random.choice(content)
        print(choice)
        return choice       
def main():
    while True:
        choice = input(f"Welcome to the Program Manager {username}, What would you like to do today?(read, write, delete, quit, random): ").lower()
        if choice == "read":
            read()
        elif choice == "write":
            write()
        elif choice == "delete":
            delete()
        elif choice == "quit":
            break
        elif username == "Hailey" and choice == "hi" or choice == "hello":
            print(f"Hello, {username}")
        elif choice == "random":
            ra()
if username == "Ash":
    main()
elif username == "J":
    main()
elif username == "Hailey":
    main()
elif username == "Austin":
    main()
elif username == "Trent":
    main()
else:
    pass



