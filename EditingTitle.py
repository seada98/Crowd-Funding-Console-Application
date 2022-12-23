import os

def editingTitle(usermail, title):
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
                        newTitle = input("Enter Your New Title : ")
                        if newTitle.isalnum():
                            newTitle = str(newTitle)
                            break
                        else:
                            print("Invalid Naming Of a Title, Try Again")
                    project_info[1] = newTitle
                    finalInfor = ":".join(project_info)
                    # print(finalInfor)
                    with open("Projects/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                        print(f"Your New Title [{newTitle}] is Successfully Added, You will back to Menu")
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
