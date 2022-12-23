import createProjects
import ViewProjects
import EditingMenu
import DeleteProject
import Searching

def loginMenu(userEmail):
    while True:
        print("Enter Your Choice Carefully As You Asked For : ")
        print("[1] Create a Project")
        print("[2] View All Projects")
        print("[3] Edit Your Own Projects")
        print("[4] Delete Your Own Project")
        print("[5] Search For a Project")
        print("[6] Back")
        print("[7] Exit")
        logginUserMail = userEmail
        choise = input("Your Choise Is : ")
        if choise.isnumeric():
            choise = int(choise)
            if choise == 1:
                createProjects.createProject(logginUserMail)
            elif choise == 2:
                ViewProjects.viewProjects(logginUserMail)
            elif choise == 3:
                EditingMenu.editingRecord(logginUserMail)
            elif choise == 4:
                title = EditingMenu.checkingtitleValidation()
                DeleteProject.deleteRecord(logginUserMail, title)
            elif choise == 5:
                title = EditingMenu.checkingtitleValidation()
                Searching.recordSearching(logginUserMail, title)
            elif choise == 6:
                return
            elif choise == 7:
                print("GoodBye ! ")
                exit()
            else:
                print("Invalid Choise, Try Again")
        else:
            print("Invalid Input")
