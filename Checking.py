def checklogin(email, password):
    with open("Users/USERS.txt") as readFile:
        users = readFile.readlines()
        for user in users:
            user = user.strip("\n")
            user_info = user.split(":")
            if user_info[2] == email and user_info[3] == password:
                return True
    return False

def checkEmail(email):
    with open("Users/USERS.txt") as readFile:
        users = readFile.readlines()
        for user in users:
            user = user.strip("\n")
            user_info = user.split(":")
            if user_info == ['']:
                break
            elif user_info[2] == email:
                print("The Email Already Exist , Please Enter Another Email")
                return False
    return True

def checkTitle(title):
    with open("Projects/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info == ['']:
                break
            elif project_info[1] == title:
                print("The Title Already Exist , Please Enter Another Title")
                return False
    return True

