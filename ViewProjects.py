def viewProjects(email):
    userMail = email
    flag = 0
    with open("Projects/projects.txt") as readFile:
        projects = readFile.readlines()
        counter = 1
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info == [""]:
                flag = 0
            else:
                if userMail == project_info[0]:
                    print(f"Project {counter} ")
                    print(f"User Email: {project_info[0]}")
                    print(f"Project Title: {project_info[1]}")
                    print(f"Description: {project_info[2]}")
                    print(f"Total target: {project_info[3]}")
                    print(f"Start Date: {project_info[4]}")
                    print(f"End Date: {project_info[5]}")
                    counter += 1
                    flag = 1

    if flag == 0:
        print("You Have No Projects Yet , You Will Back To Menu ")
