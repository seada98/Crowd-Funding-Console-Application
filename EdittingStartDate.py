import os
import datetime

def editStartDate(usermail, title):
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
                        newDate = input("Enter Your New Start Date : ")
                        try:
                            datetime.datetime.strptime(newDate, '%Y-%m-%d')
                            break
                        except ValueError:
                            print("Incorrect Data Format, Should Be YYYY-MM-DD")
                    project_info[4] = newDate
                    finalInfor = ":".join(project_info)
                    with open("Projects/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                        print(f"Your New Date [{newDate}] is Successfully Added")
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
        print(f"We Can Not Found a Title With This Name [{projectTitle}]")
    os.remove("Projects/projects.txt")
    os.rename("Projects/temp.txt", "Projects/projects.txt")
