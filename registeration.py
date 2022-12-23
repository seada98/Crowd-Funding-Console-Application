import inserting
import Checking
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def nameValidation(varname):
    att = input(f"Enter Your {varname} : ").strip()
    if att.isalpha():
        return att
    else:
        return nameValidation(varname)

def emailValidation(Email):
    Email = input("Enter Your Mail : ").strip()
    if re.fullmatch(regex, Email):
        if Checking.checkEmail(Email):
            return Email
        else:
            return emailValidation(Email)
    else:
        print("Invalid Email Type , Please Try Again ")
        return emailValidation(Email)

def passValidation(password):
    Password = input(f"Enter your Password : ").strip()

    SpecialSym = ['$', '@', '#', '_', '-', '!', '%', '&']
    val = True

    if len(Password) < 6:
        print('Length Should Be At Least 6')
        val = False

    if len(Password) > 20:
        print('Length Should Be Not Be Greater Than 8')
        val = False

    if not any(char.isdigit() for char in Password):
        print('Password Should Have At Least One Numeral')
        val = False

    if not any(char.isupper() for char in Password):
        print('Password Should Have At Least One Uppercase Letter')
        val = False
    if not any(char.islower() for char in Password):
        print('Password Should Have At Least One Lowercase Letter')
        val = False

    if not any(char in SpecialSym for char in Password):
        print('Password Should Have At Least One Of The Symbols [$@#_-!%&]')
        val = False
    if val:
        return Password
    else:
        return passValidation(Password)

def conPassValidation(password):
    cofPassword = input("Confirm Your Password : ")

    if password == cofPassword:
        return cofPassword
    else:
        print("Not Matched Password , Please Try Again")
        return conPassValidation(password)

def phoneNumValidation(phoneNum):
    number = input("Please Enter Your Phone Number : ")
    if len(number) < 11 or len(number) > 11:
        print("Please Enter a Valid Phone Number")
        return phoneNumValidation(phoneNum)
    else:
        if number.startswith('010') or number.startswith('011') or number.startswith('012') or number.startswith('015'):
            return number
        else:
            print("Invalid Number in Egypt , Please Enter A Valid Number")
            return phoneNumValidation(phoneNum)

def registerationForm():
    fname = nameValidation("fname")
    lname = nameValidation("lname")
    Email = emailValidation("Email")
    password = passValidation("password")
    conPassword = conPassValidation(password)
    phoneNum = phoneNumValidation("phoneNum")
    userInfo = [fname, lname, Email, password, conPassword,phoneNum]
    inserting.insert(userInfo)
    return
