def askpass():
    password = input("enter password: ")
    return password
    
def checkpass(password):
    entry = input("Enter your password")
    if entry == password:
        print("Correct password")
    else:
        print("Incorrect Password")

def collecting(password1, password2):
    while(True):
        selection = input("Enter key holder:")
        if selection == "1":
            checkpass(password1)
        elif selection == "2":
            checkpass(password2)
def store():
    password  = askpass()
    return password    

password = 0
password2 = 0
while(True):
    Choice = input("Are you collection or Inputting ?")
    if Choice.lower() == "inputting":
        holder = input("Enter holder")
        if holder == "1":
            password = store()
        elif holder == "2":
            password2 = store()
    elif Choice.lower() == "collecting":
        collecting(password,password2)
