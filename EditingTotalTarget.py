import os

def editingTotalTarget(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    with open("Projects/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    while True:
                        newTotal = input("Enter Your New Total Target : ")
                        if newTotal.isnumeric():
                            newTotal = str(newTotal)
                            break
                        else:
                            print("Invalid type of a Total Target, Try again")
                    project_info[3] = newTotal
                    finalInfor = ":".join(project_info)
                    # print(finalInfor)
                    with open("Projects/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                        print(f"Your New Total Target [{newTotal}] is Successfully added")
                        flag = 1
                else:
                    project_info = ":".join(project_info)
                    with open("Projects/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("Projects/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
        print(f"We can not found a title with this name [{projectTitle}]")
    os.remove("Projects/projects.txt")
    os.rename("Projects/temp.txt", "Projects/projects.txt")
