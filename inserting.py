def insert(userInfo):
    userInfo = ":".join(userInfo)
    with open("Users/USERS.txt", "a") as userFile:
        data = userInfo.strip("\n")
        data = f"{data}\n"
        userFile.write(data)
        print("You Have Register Successfully, You will back to Main Menu to login !")

