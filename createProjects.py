import Checking
import addnewProjects
import datetime

def titleValidation(title):
    projTitle = input("Enter Your Project Title : ").strip()
    if projTitle.isalpha():
        if Checking.checkTitle(projTitle):
            return projTitle
        else:
            return titleValidation(title)
    else:
        return titleValidation(title)

def totalTargetValidation(details):
    projDetails = input("Your Total Target : ")
    if projDetails.isnumeric():
        projDetails = str(projDetails)
        return projDetails
    else:
        print("Invalid Input ")
        return totalTargetValidation(details)

def startDateValidation(date):
    startDate = input(f"Enter Project {date} Date As (YYYY-MM-DD) :  ")
    try:
        datetime.datetime.strptime(startDate, '%Y-%m-%d')
        return startDate
    except ValueError:
        print("Incorrect Data Format, Should Be YYYY-MM-DD")
        return startDateValidation(date)

def endDateValidation(start):
    endDate = input(f"Enter Project End Date: ")
    try:
        datetime.datetime.strptime(endDate, '%Y-%m-%d')
        if start < endDate:
            return endDate
        else:
            print("End Date Can Not Be Before Start Date")
            return endDateValidation(start)
    except ValueError:
        print("Incorrect Data Format, Should Be YYYY-MM-DD")
        return endDateValidation(start)

def createProject(userMail):
    userEmail = userMail
    title = titleValidation("title")
    details = input("Project Details : ")
    totalTarget = totalTargetValidation("totalTarget")
    Start = startDateValidation("Start")
    End = endDateValidation(Start)
    projInfo = [userEmail, title, details, totalTarget, Start, End]
    addnewProjects.addProject(projInfo)
    return
