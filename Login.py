import Checking
import LoginMenu

def login():
    Email = input("Enter Your Email:").strip()
    Password = input("Enter Your Password:").strip()
    if Checking.checklogin(Email, Password):
        print("Loging Successfully !")
        LoginMenu.loginMenu(Email)
        return True
    print("Invalid Username or Email , Please Try Again")
    return login()