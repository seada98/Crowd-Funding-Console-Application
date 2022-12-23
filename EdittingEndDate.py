import os
import datetime

def editEndDate(usermail, title):
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
                        endDate = input("Enter Your New End Date : ")
                        try:
                            datetime.datetime.strptime(endDate, '%Y-%m-%d')
                            if project_info[4] < endDate:
                                break
                            else:
                                print("End date can not be before Start date")
                        except ValueError:
                            print("Incorrect data format, should be YYYY-MM-DD")
                    project_info[5] = endDate
                    finalInfor = ":".join(project_info)
                    with open("Projects/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                        print(f"Your New Date [{endDate}] is Successfully Added")
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
