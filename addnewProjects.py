def addProject(projectInfo):
    finalInfor = ":".join(projectInfo)
    with open(f"Projects/projects.txt", "a") as projectFile:
        data = finalInfor.strip("\n")
        data = f"{data}\n"
        projectFile.write(data)
        print("You Have Add Project Successfully , You Will Back To Menu")
    return
