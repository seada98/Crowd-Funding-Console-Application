import registeration
import Login

print("Welcome To Crowd-Funding Console Application")
def mainFun():
    while True:
        print("Choise Foom List Blow : ")
        print("[1] Registration")
        print("[2] Login")
        print("[3] Exit")
        Choise = input("Enter Your Choise : ").strip()
        if Choise.isnumeric():
            Choise = int(Choise)
            if Choise == 1:
                print("You Now In Registeration Mode ")
                registeration.registerationForm()
            elif Choise == 2:
                print("You Now in Login Mode ")
                Login.login()
            elif Choise == 3:
                print("GoodBye ! ")
                exit()
            else:
                print("Invalid Input")

        else:
            print("You Enter Invalid Input")

mainFun()
