import re

class Person:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPassword: ########"
    
registers = []

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_password(password):

    if len(password) < 8:
        print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9]',password) is None:
        print("Make sure your password has a number in it")
    elif re.search('[A-Z]',password) is None: 
        print("Make sure your password has a capital letter in it")
        return False
    else:
        return True
    
def register():
    while True:
        sign_up = input("Do you want to Sign up! 'Yes' or 'No': \n")

        if sign_up.lower() != 'yes':
            print("Thank you!")
            break        

        name = input("What's your name: ")

        while True:
            email = input("What's your email: ")
            if not is_valid_email(email):
                print("Invalid email format. Please enter a valid email.")
            else:
                break

        while True:
            password = input("Your secret code ;): ")
            if is_valid_password(password):
                break 
            else:
                print("Please enter a password that meets all the requirements.")  

        registers.append(Person(name, email, password))
        print("Registration successful!\n")

def login():

    while True:
        name = input("Input your name: \n")
        email = input("Input your email: \n")
        password = input("Input your password: \n")

        for user in registers:
            if name == user.name and email == user.email and password == user.password:
                print("Welcome to the main page")
                while True:
                    stop = input("Q to quit: \n")
                    if stop.lower() == "q":
                        return

            else:
                print("Error name,email or password")
                break


print("Welcome to the login App")

while True:
    print("\nMenu:")
    print("1. Sign Up")
    print("2. Login")
    print("3. View user!")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        register()
    if choice == "2":
        login()
    elif choice == "3":
        for person in registers:
            print(person)
        else:
            print("\nThere's no users")
    elif choice == "4":
        print("Thank you for using Login App!")
        break
