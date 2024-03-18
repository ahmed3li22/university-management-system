# some partner file, if you want to check it functions go open it
# it saves Students complaints in a json file btw so data wont dissapear after you exit the programme
from ComplaintsManagement import Col, writepargraph, load_complaints, save_complaints, submit_complaint, view_complaints, remove_complaint

# just a Colors class that used for making output with colors
# works like a string concatination
# for examble Col.BLUE+ "some test" + Col.RESET
#(reset for reseting color after if you didnt write it text will remain with same color)
class Col:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'



option=1000

# this 3 functions just for checking values user enter, it takes value and if these values it not what it should be
# it will get user in a while loop tells him to enter a valid value untill he enter it
def AorBChecker(value):
    while value not in ["A", "B"]:
        print(Col.RED+"only (A) or (B) to write dont write anything alse"+Col.RESET)
        value = input(Col.RED+"rechoose your Group: "+Col.RESET)

    return value

def digitchecker(digitvalue):
    while True:
        if digitvalue.isdigit():
            return digitvalue
        else :
            print(Col.RED+"do not write any character only numbers"+Col.RESET)
            digitvalue=input(Col.RED+"rewrite your input: "+Col.RESET)


def yesnochecker(value):
    while value not in ["yes", "no"]:
        print(Col.RED+"only (yes) or (no) to write dont write anything alse"+Col.RESET)
        value = input(Col.RED+"rewrite your option: "+Col.RESET)

    return value


#===========================COURSES CLASS=====================================
class Courses:
    CoursesList=[]
    CoursesName=[]
    CoursesCode=[]
    CoursesNumber=0
    def __init__(self,CourseName,Hours,AcademicYear,CourseCode,MaxA,MaxB):
        self.__name=CourseName
        self.__Hours=Hours
        self.__CourseCode=CourseCode
        self.__AcademicYear=AcademicYear
        self.__MaxA=MaxA
        self.__MaxB=MaxB
        Courses.CoursesList.append(self)
        Courses.CoursesName.append(self.__name)
        Courses.CoursesCode.append(self.__CourseCode)
        Courses.CoursesNumber+=1

    def GetName(self):
        return self.__name
    def GetHours(self):
        return self.__Hours
    def GetCourseCode(self):
        return self.__CourseCode
    def GetAcademicYear(self):
        return self.__AcademicYear
    def GetAmax(self):
        return self.__MaxA
    def GetBmax(self):
        return self.__MaxB
    def ReduceAmax(self):
        self.__MaxA-=1
    def ReduceBmax(self):
        self.__MaxB-=1
    def GetFullCourseInfo(self,StudentGroup=None):
        if StudentGroup==None:
            print(Col.YELLOW + "=================================================" + Col.RESET)
            print(Col.BLUE+f"CourseName:{self.__name}, CourseCode:{self.__CourseCode}, Course Hours:{self.__Hours}"+Col.RESET)
            print(Col.BLUE+f"AcademicYear:{self.__AcademicYear}, AvilablePlaces in group A:{self.__MaxA}, AvilablePlaces in group B:{self.__MaxB}"+Col.RESET)
            print(Col.YELLOW + "=================================================" + Col.RESET)
        elif StudentGroup !=None:
            print(Col.YELLOW + "=================================================" + Col.RESET)
            print(Col.BLUE+f"CourseName:{self.__name}, CourseCode:{self.__CourseCode}, Course Hours:{self.__Hours}"+Col.RESET)
            print(Col.BLUE+f"AcademicYear:{self.__AcademicYear}, AvilablePlaces in group A:{self.__MaxA}, AvilablePlaces in group B:{self.__MaxB}"+Col.RESET)
            print(Col.BLUE+f"Course Group:{StudentGroup}"+Col.RESET)
            print(Col.YELLOW + "=================================================" + Col.RESET)

    def ShowAvilableCourses():
        print(Col.BLUE+f"Courses Number: {Courses.CoursesNumber} "+Col.RESET)
        for i in range(0,len(Courses.CoursesList)):
            Courses.CoursesList[i].GetFullCourseInfo()


#======================================NEWS AND ANNOUCMENTS CLASS===============================
class News:
    Annoucments=0
    Annoucments_list=[]
    Annoucments_titles=[]
    def __init__(self,title,content):
        self.__title=title
        self.__content=content
        News.Annoucments+=1
        News.Annoucments_list.append(self)
        News.Annoucments_titles.append(self.__title)
    def GetTitle(self):
        return self.__title
    def GetContent(self):
        return self.__content
    @classmethod
    def ShowNews(cls):
        if len(News.Annoucments_list)==0:
            print(Col.BLUE+"\n======================="+Col.RESET)
            print(Col.BLUE+"There is no Annoucments"+Col.RESET)
            print(Col.BLUE+"=======================\n"+Col.RESET)
        for i in range(0,len(News.Annoucments_list)):
            print(Col.BLUE+"=========================================="+Col.RESET)
            print(Col.BLUE+f"                 {News.Annoucments_list[i].GetTitle()}               "+Col.RESET)
            print(Col.BLUE+f"\n{News.Annoucments_list[i].GetContent()}")
            print(Col.BLUE+"=========================================="+Col.RESET)

#=======================STUDENT CLASS=========================
class Student:
    listofnames = []
    ListofIDs = []
    def __init__(self,username,age,id,phonenumber,password):
        self.__name=username
        self.__age=age
        self.__id=id
        self.__phonenum=phonenumber
        self.__password=password
        self.__academicyear=1
        self.__gpa=0
        self.__StudentCourses = []
        self.__StudentCoursesNames = []
        self.__CoursesGroups = []
        Student.listofnames.append(username)
        Student.ListofIDs.append(id)
#===============Getter functions============================
    def getinfo(self):
        print(self.__name,"                 ",self.__id,)
    def getname(self):
        return self.__name
    def getid(self):
        return self.__id
    def getphone(self):
        return self.__phonenum
    def getpassword(self):
        return self.__password
    def getgpa(self):
        return self.__gpa
    def getstudentcourses(self):
        return self.__StudentCourses
    def getstudentcoursesnames(self):
        return self.__StudentCoursesNames
    def getcoursesgroups(self):
        return self.__CoursesGroups
    def getfullinfo(self):
        print(Col.BLUE+f"name:{self.__name}",f"age:{self.__age}",f"id:{self.__id}",f"phonenum:0{self.__phonenum}",f"gpa:{self.__gpa}",f"academicyear:{self.__academicyear}"+Col.RESET,sep="\n")
#=================Setter functions================
    def nameset(self,newname):
        self.__name=newname
    def ageset(self,newage):
        self.__age=newage
    def idset(self,newid):
        self.__id=newid
    def passwordset(self,newpassword):
        self.__password=newpassword
    def phonenumset(self,newphonenum):
        self.__phonenum=newphonenum
    def academicyearset(self,newacademicyear):
        self.__academicyear=newacademicyear
    def gpaset(self,newgpa):
        self.__gpa=newgpa
#==============login function=================================
    def login(self,userid,password):
        if self.__id==userid and self.__password==password:
            return self,True
        else:
            return None,False
#=================Edit information Functions==================
    def changestudentdata(self,optionlist):
        for i in range(0,len(optionlist)):
            if optionlist[i]==1:
                newpassword=input(Col.BLUE+"Enter your New password:"+Col.RESET)
                self.passwordset(newpassword)
                print(Col.GREEN+"\nPassword Changed Successfully\n"+Col.RESET)
            elif optionlist[i]==2:
                newphonenumber=int(digitchecker(input(Col.BLUE+"Enter your New Phonenumber:"+Col.RESET)))
                self.phonenumset(newphonenumber)
                print(Col.GREEN + "\nNumber Changed Successfully\n" + Col.RESET)
            elif optionlist[i]==3:
                newage=int(digitchecker(input(Col.BLUE+"Enter your new age:"+Col.RESET)))
                print(Col.GREEN + "\nAge Changed Successfully\n" + Col.RESET)
                self.ageset(newage)
        return

    def editinformation(self):
        optionslist=[]
        while True:
            print(Col.BLUE+"\nChange password => 1"+Col.RESET)
            print(Col.BLUE+"Change PhoneNumber => 2"+Col.RESET)
            print(Col.BLUE+"Change age => 3")
            print(Col.BLUE+"Back =>4"+Col.RESET)
            Choice=int(digitchecker(input(Col.BLUE+"Choose your Choice: "+Col.RESET)))
            if Choice==4:
                break
            if Choice not in [1,2,3]:
                print(Col.Red+"\nInvalid Choice, rechoose\n"+Col.RESET)
                continue
            elif Choice in optionslist:
                print(Col.RED+"\nChoice already exist\n"+Col.RESET)
                continue
            optionslist.append(Choice)
            while True:
                yesnooption = "None"
                yesnooption = yesnochecker(input(Col.BLUE + "change any thing alse ? (yes/no):" + Col.RESET))
                if yesnooption.lower() == "no":
                    Student.changestudentdata(self,optionslist)
                    return
                elif yesnooption.lower() == "yes":
                    break
#==============Manage Courses for Student functions============
    def AddStudentCourses(obj):
        CourseName=input(Col.BLUE+"Enter Course Name you want to add: "+Col.RESET)
        CourseCode=input(Col.BLUE+"Enter Course Code you want to add: "+Col.RESET)
        if (CourseName not in Courses.CoursesName) and (CourseCode not in Courses.CoursesCode) :
            print(Col.RED+"Course Not Found, recheck course name and code before writing"++Col.RESET)
            return
        for i in range(0,len(Courses.CoursesList)):
            if Courses.CoursesList[i].GetName()==CourseName:
                CourseGroup = AorBChecker(input(Col.BLUE+"Choose Course Group (A/B) : "+Col.RESET))
                if Courses.CoursesList[i].GetAmax()==0 and Courses.CoursesList[i].GetBmax()==0:
                    print(Col.RED+"No Avilable Space for this Course Groups"+Col.RESET)
                    return
                while Courses.CoursesList[i].GetAmax()==0 and CourseGroup=='A':
                    CourseGroup=AorBChecker(input(Col.YELLOW+"Group A is full, Choose Group B"+Col.RESET))
                while Courses.CoursesList[i].GetBmax()==0 and CourseGroup=='B':
                    CourseGroup=AorBChecker(input(Col.YELLOW+"Group B is full, Choose Group A"+Col.RESET))
                obj.getcoursesgroups().append(CourseGroup)
                obj.getstudentcourses().append(Courses.CoursesList[i])
                obj.getstudentcoursesnames().append(Courses.CoursesList[i].GetName())
                if CourseGroup=='A':
                    Courses.CoursesList[i].ReduceAmax()
                elif CourseGroup=='B':
                    Courses.CoursesList[i].ReduceBmax()
                print(Col.GREEN+"Course Added Successfully"+Col.RESET)
                return

    def ShowStudentCourses(obj):
        if len(obj.getstudentcourses())==0:
            print(Col.BLUE+"You didnt add any Courses Yet\n"+Col.RESET)
        for i in range(0,len(obj.getstudentcourses())):
            obj.getstudentcourses()[i].GetFullCourseInfo(obj.getcoursesgroups()[i])

    def RemoveStudentCourses(obj):
        CourseName=input(Col.BLUE+"Enter Course Name you want to remove from your list: "+Col.RESET)
        if CourseName not in obj.getstudentcoursesnames():
            print(Col.RED+"Course Not Found pls recheck"+Col.RESET)
            return
        target="None"
        for i in range(0,len(obj.getstudentcourses())):
            if CourseName==obj.getstudentcourses()[i].GetName():
                target=obj.getstudentcourses()[i]
                CourseGroup=obj.getcoursesgroups()[i]
        if target!="None":
            obj.getstudentcoursesnames().remove(target.GetName())
            obj.getstudentcourses().remove(target)
            obj.getcoursesgroups().remove(CourseGroup)
            print(Col.GREEN+"Course Removed Successfully"+Col.RESET)
            return


#===============================CONTROL CLASS=============================

class Control:
    listObjs = []
    def __init__(self):
        self.__username="admin"
        self.__password="12345"
    # basic login checker returns true if the passed parametars are equal to the obj attributes
    def login(self,username,password):
        if username==self.__username and password==self.__password:
            return True
    # it adds students objs that gets created in the list to save student and iterate between them
    def addnewstudent(Student):
        Control.listObjs.append(Student)
    # a function that iterates between objs in the listobjs list and calls a method that gets all information
    def getsystemdata():
        print(Col.YELLOW+"Name                       id"+Col.RESET)
        for i in range (0,len(Control.listObjs)):
            Control.listObjs[i].getinfo()
    # a while loop function that tells you do u want to sign in as student or admin
    # if you choose student two class functions will be called
    # first one checks if you already exist in the listObjs list or not by checking id
    # second one checks if the input data is true or not
    # if every thing is fine and student entered the data correct it will return the student obj and a number which is (2)

    # if the user choosed admin it will just if entered data is correct or not using login function
    # if data is correct it will returns a Number which is (3) and a None value
    # the None value here just to prevent error code
    def loginmenu():
        option=100
        while True:
            print(Col.BLUE+"\n\nsign in as Student =>1"+Col.RESET)
            print(Col.BLUE+"sign in as admin ==>2"+Col.RESET)
            print(Col.BLUE+"Exit ==> 0"+Col.RESET)
            option=int(digitchecker(input(Col.BLUE+"?: "+Col.RESET)))
            if option==1:
                print(Col.BLUE+"\nsing in with your id and password"+Col.RESET)
                print(Col.BLUE+"if its your first sign in, your password should be created by the admin"+Col.RESET)
                userid=int(digitchecker(input(Col.BLUE+"userid: "+Col.RESET)))
                password=input(Col.BLUE+"password: "+Col.RESET)
                result2=Control.getstudentobj(Control.listObjs, userid)
                if not result2:
                    continue
                result=Student.login(result2,userid,password)
                if result[1]==True:
                    return result[0],2
                else:
                    print(Col.RED+"\ninvalid userid or password pls retry\n"+Col.RESET)
            elif option==2:
                username=input(Col.BLUE+"username: "+Col.RESET)
                password=input(Col.BLUE+"password: "+Col.RESET)
                if Control.login(Control(),username,password):
                    return 3,None
                else:
                    print(Col.RED+"invalid username or password pls retry"+Col.RESET)
            elif option==0:
                exit()
    # this function works by taking Student Name (i wont make it with id cus some students does not have id sometime)
    # and then checks if the student in the ids list of student class or not
    # if student exist it will iterate between objs in Control class and once it find the id
    # it will assign it to a target variable and then delet that target from the list
    def removestudent(cls,Stusername):
        target="none"
        if (Stusername not in Student.listofnames):
            print(Col.RED+"\nStudent not found\n"+Col.RESET)
        for i in range(0,len(Control.listObjs)):
            if Stusername==Control.listObjs[i].getname() :
                print(Col.GREEN+"Student removed "+Col.RESET)
                target=Control.listObjs[i]
        if target!="none":
            Control.listObjs.remove(target)
    # this function just checks if user exist or not by checking id , if it exist will return the obj
    def getstudentobj(objlist,userid):
        if userid not in Student.ListofIDs:
            print(Col.RED+"Userid not found"+Col.RESET)
            return False
        for i in range(0,len(objlist)):
            if objlist[i].getid()==userid:
                return objlist[i]
    # this function for getting user information , iterate between listObjs and if name found it will call getfullinfo student class
    def getastudent(cls,Stusername):
        if Stusername in Student.listofnames:
            for i in range(0,len(Control.listObjs)):
                if Stusername==Control.listObjs[i].getname():
                    print(Col.YELLOW+"\n\n==================================","Student data","=================================="+Col.RESET, sep="\n")
                    Control.listObjs[i].getfullinfo()
                    print("\n\n")
                    return Control.listObjs[i]
                    break
        else:
            print(Col.RED+"Student not found, recheck the name\n\n"+Col.RESET)
            return False

    # the next two functions works as following:
    # first one is editmenu, it asks the user what information he wants to edit, if the value he choses is repeated or does not exist
    # it will return an error message for him and then gets back at the begining of the loop
    # if the values he entered are fine, the change student data will get that student obj and list of options user choosed
    # then depend on the vale of each index of this list it will activate the conditions and let user set new data

    def changestudentdata(cls,obj,optionlist):
        for i in range(0,len(optionlist)):
            if optionlist[i]==1:
                newname=input(Col.BLUE+"enter new name:"+Col.RESET)
                for i in range(0,len(Student.listofnames)):
                    if Student.listofnames[i]==obj.getname():
                        Student.listofnames[i]=newname
                obj.nameset(newname)
            elif optionlist[i]==2:
                newage=int(digitchecker(input(Col.BLUE+"enter new age:"+Col.RESET)))
                obj.ageset(newage)
            elif optionlist[i]==3:
                newid=int(digitchecker(input(Col.BLUE+"enter new id:"+Col.RESET)))
                for i in range(0,len(Student.ListofIDs)):
                    if Student.ListofIDs[i]==obj.getid():
                        Student.ListofIDs[i]=newid
                obj.idset(newid)
            elif optionlist[i]==4:
                newphonenumber=int(digitchecker(input(Col.BLUE+"enter new phonenumber:"+Col.RESET)))
                obj.phonenumset(newphonenumber)
            elif optionlist[i]==5:
                newacademicyear=int(digitchecker(input(Col.BLUE+"enter new academic year:"+Col.RESET)))
                obj.academicyearset(newacademicyear)
            elif optionlist[i]==6:
                newstupassword=input(Col.BLUE+"enter new student password:"+Col.RESET)
                obj.passwordset(newstupassword)
            elif optionlist[i]==7:
                newgpa=int(digitchecker(input(Col.BLUE+"enter new student gpa: "+Col.RESET)))
                obj.gpaset(newgpa)
        print(Col.GREEN+"Student Changed\n"+Col.RESET)
        print(Col.YELLOW+"==================================","Student data", "=================================="+Col.RESET,sep="\n")
        obj.getfullinfo()
        print("\n\n")
    def editstudentmenu(cls,Student):
        print(Col.BLUE+"what data you want to change"+Col.RESET)
        optionlist=[]
        option=100
        while True:
            flag = True
            print("\n\n")
            print(Col.BLUE+"name ==> 1"+Col.RESET)
            print(Col.BLUE+"age ==> 2"+Col.RESET)
            print(Col.BLUE+"id ==> 3"+Col.RESET)
            print(Col.BLUE+"phonenumber ==> 4"+Col.RESET)
            print(Col.BLUE+"academic year ==> 5"+Col.RESET)
            print(Col.BLUE+"password ==> 6"+Col.RESET)
            print(Col.BLUE+"gpa ==> 7"+Col.RESET)
            print(Col.BLUE+"to cancel ==> 0"+Col.RESET,sep="\n")
            option=int(digitchecker(input(Col.BLUE+"Enter the option: "+Col.RESET)))
            print("\n\n")
            if option==0:
                return False
            if option not in [1,2,3,4,5,6,0,7]:
                print(Col.RED+"option not found pls rechose \n\n"+Col.RESET)
                continue
            for i in range (0,len(optionlist)):
                if option in optionlist:
                    print(Col.RED+f"option Number {i+1} you chosed is repeated pls rechose it"+Col.RESET)
                    flag=False
            if flag:
                if option in [1,2,3,4,5,6,7]:
                    optionlist.append(option)
                while True:
                    yesnooption="None"
                    yesnooption=yesnochecker(input(Col.BLUE+"change any thing alse ? (yes/no):"+Col.RESET))
                    if yesnooption.lower()=="no":
                        return Student,optionlist
                    elif  yesnooption.lower()=="yes":
                        break
    #=================================post news functions=============================
    def add_news():
        news_title = input(Col.BLUE + "Enter the title of the annoucment: " + Col.RESET)
        if news_title in News.Annoucments_titles:
            print(Col.RED + "This Annoucment is already added" + Col.RESET)
            return False
        news_content = ""
        print(Col.BLUE + "Enter the content of the annoucment , to stop writing write \"exit\" " + Col.RESET)
        while True:
            line = input("")
            if line.lower() == 'exit':
                break
            news_content += line + '\n'
        Newannoucment = News(news_title, news_content)
        print(Col.GREEN + "Annoucment added successfully!" + Col.RESET)

    def Remove_news(News_title):
        target = 'None'
        if News_title not in News.Annoucments_titles:
            print(Col.RED + "Title not found" + Col.RESET)
            return False
        for i in range(0, len(News.Annoucments_list)):
            if News_title == News.Annoucments_list[i].GetTitle():
                print(Col.GREEN + "Annoucment Removed" + Col.RESET)
                target = News.Annoucments_list[i]
        if target != 'None':
            News.Annoucments_titles.remove(target.GetTitle())
            News.Annoucments_list.remove(target)

    #=======================Manage Courses Functions======================================
    def AddCourse():
        CourseName = input(Col.BLUE + "Enter Course name: " + Col.RESET)
        if CourseName in Courses.CoursesName:
            print(Col.RED + "\nThis Course already exist\n" + Col.RESET)
            return
        CourseHours = int(input(Col.BLUE + "Enter Course Hours: " + Col.RESET))
        CourseCode = input(Col.BLUE + "Enter Course Code: " + Col.RESET)
        AcademicYear = input(Col.BLUE + "Enter the AcademicYear of the Course: " + Col.RESET)
        GroupAmax = int(input(Col.BLUE + "Enter max capacity of Group A: " + Col.RESET))
        GroupBmax = int(input(Col.BLUE + "Enter max capacity of Group B: " + Col.RESET))
        NewCourse = Courses(CourseName, CourseHours, AcademicYear, CourseCode, GroupAmax, GroupBmax)
        print(Col.GREEN + "\nCourse added Successfully!\n" + Col.RESET)

    def RemoveCourse():
        CourseName = input(Col.BLUE + "Enter Course name you want to remove: " + Col.RESET)
        if CourseName not in Courses.CoursesName:
            print(Col.RED + "\nCourse Not found\n" + Col.RESET)
            return
        target = "None"
        for i in range(0, len(Courses.CoursesList)):
            if CourseName == Courses.CoursesList[i].GetName():
                target = Courses.CoursesList[i]
        if target != "None":
            for i in range(0,len(Control.listObjs)):
                for j in range (0,len(Control.listObjs[i].getstudentcoursesnames())):
                    if Control.listObjs[i].getstudentcoursesnames()[j]==target.GetName():
                        Control.listObjs[i].getstudentcourses().remove(target)
                        Control.listObjs[i].getcoursesgroups().remove(Control.listObjs[i].getcoursesgroups()[j])
                        Control.listObjs[i].getstudentcoursesnames().remove(target.GetName())
                        break
            Courses.CoursesName.remove(target.GetName())
            Courses.CoursesList.remove(target)
            print(Col.GREEN + "\nCourse Removed Successfully\n" + Col.RESET)
            Courses.CoursesNumber -= 1






#==========================================================================
#========================OUT OF CLASS======================================
#==========================================================================

# manage courses option for admin panel
# Note: if you remove a course it will get deleted in every student registered Courses
# if you want to see each called function go look for it in classes

def ManageCourses():
    option=100
    while True:
        print(Col.BLUE+"\nShow Assigned Courses >>1"+Col.RESET)
        print(Col.BLUE+"Add Course >>2"+Col.RESET)
        print(Col.BLUE+"Remove Course >>3"+Col.RESET)
        print(Col.BLUE+"Back >>4"+Col.RESET)
        print(Col.BLUE+"Exit >>0\n"+Col.RESET)
        option=int(digitchecker(input(Col.BLUE+"Enter your Choice :"+Col.RESET)))

        if option==4:
            return
        elif option==0:
            exit()
        elif option==1:
            if len(Courses.CoursesList)==0:
                print(Col.BLUE+"\nNo Courses are added\n"+Col.RESET)
                continue
            print(Col.BLUE+"================Avilable Courses================\n"+Col.RESET)
            Courses.ShowAvilableCourses()
            print("\n\n")
        elif option==2:
            Control.AddCourse()
        elif option==3:
            Control.RemoveCourse()
        else:
            print(Col.RED+"\nInvalid Choice, retry\n"+Col.RESET)

# this function for student panel, it takes a parametar which is the student obj
#it calls different class functions depend on the value you enter
# go look for functions that been called in classes if you want to see what it does

def ManageCoursesForStudents(obj):
    while True:
        print(Col.BLUE+"\n\nSee Avilable Courses >> 1"+Col.RESET)
        print(Col.BLUE+"See Registered Courses >> 2"+Col.RESET)
        print(Col.BLUE+"Add Course >> 3"+Col.RESET)
        print(Col.BLUE+"Remove Course >> 4"+Col.RESET)
        print(Col.BLUE+"Back >> 5"+Col.RESET)
        print(Col.BLUE+"Exit >> 0\n"+Col.RESET)
        option=int(digitchecker(input(Col.BLUE+"Choose your Choice : "+Col.RESET)))
        print("\n\n")
        if option==5:
            return
        elif option==0:
            exit()
        elif option==1:
            if len(Courses.CoursesList)==0:
                print(Col.BLUE+"\nNo Courses are added\n"+Col.RESET)
                continue
            Courses.ShowAvilableCourses()
        elif option==2:
            Student.ShowStudentCourses(obj)
        elif option==3:
            Student.AddStudentCourses(obj)
        elif option==4:
            Student.RemoveStudentCourses(obj)


#this function for manage option , it contains some functionalities, any option you will choose will call some class functions
# to see what every class function does go back to classes and look for it

def managestudents():
    option=100
    while True:
        print(Col.BLUE+"show students >>1"+Col.RESET)
        print(Col.BLUE+"edit student information >>2"+Col.RESET)
        print(Col.BLUE+"search for a student >>3"+Col.RESET)
        print(Col.BLUE+"back window befoe this >>4"+Col.RESET)
        print(Col.BLUE+"exit >>0"+Col.RESET)
        option = int(digitchecker(input(Col.BLUE+"Enter your option: "+Col.RESET)))
        if option==0:
            exit()
        elif  option==4:
            return
        elif option==1:
            print("\n\n")
            print(Col.YELLOW+"===========================", f"Students data   students number:{len(Control.listObjs)}","==========================="+Col.RESET, sep="\n")
            Control.getsystemdata()
            print("\n\n")
        elif option==2:
            studentname=input(Col.BLUE+"Enter student name:"+Col.RESET)
            result1=Control.getastudent(Control(),studentname)
            if not result1:
                continue
            result2=Control.editstudentmenu(Control(),result1)
            if not result2:
                continue
            Control.changestudentdata(Control(),result2[0],result2[1])
        elif option==3:
            studentname=input(Col.BLUE+"Enter student name:"+Col.RESET)
            result1=Control.getastudent(Control(),studentname)
            if not result1:
                continue
            while True:
                print(Col.BLUE+"to edit the student >>1"+Col.RESET)
                print(Col.BLUE+"remove the student >>2"+Col.RESET)
                print(Col.BLUE+"to get back last window >>3"+Col.RESET)
                print(Col.BLUE+"Exit >>0\n"+Col.RESET)
                option2=int(digitchecker(input(Col.BLUE+"Choose your option: "+Col.RESET)))
                if option2==1:
                    result2=Control.editstudentmenu(Control(),result1)
                    if not result2:
                        continue
                    Control.changestudentdata(Control(),result2[0],result2[1])
                    break
                elif option2==2:
                    Control.removestudent(Control(),studentname)
                    break
                elif option2==3:
                    break
                elif option2==0:
                    exit()


# main function, most of the things happen here, first run a while loop with control loginmenu to see whether your a student or a admin
# depend on the return value of the login function one of two other nested while loop will get activated
# the if conditions for sending a message lets you know that you signed in successfully
# the nested while loops keep running untill you choose exit or sign out

def main1():
    while True:
        result=Control.loginmenu()
        if result[0]==3:
            print(Col.GREEN+"Access Granted"+Col.RESET)
        while result[0]==3:
            print(Col.BLUE+"\n\nto add a new student chose >> 1"+Col.RESET)
            print(Col.BLUE+"to remove a student chose >> 2"+Col.RESET)
            print(Col.BLUE+"to manage student >> 3"+Col.RESET)
            print(Col.BLUE+"Post news >> 4"+Col.RESET)
            print(Col.BLUE+"manage Courses >> 5"+Col.RESET)
            print(Col.BLUE+"View Students Complaints >>6"+Col.RESET)
            print(Col.BLUE+"to sign out >> 7"+Col.RESET)
            print(Col.BLUE+"to exit choose >> 0"+Col.RESET)
            option=int(digitchecker(input(Col.BLUE+"? : "+Col.RESET)))
            print("\n\n")
            if option==0 :
                exit()
            elif option==7:
                break
            elif option==1:
                nameset=input(Col.BLUE+"enter student name :"+Col.RESET)
                ageset=int(digitchecker(input(Col.BLUE+"enter student age: "+Col.RESET)))
                idseter=int(digitchecker(input(Col.BLUE+"enter student id: "+Col.RESET)))
                phonenumseter=int(digitchecker(input(Col.BLUE+"enter student phonenumber: "+Col.RESET)))
                passwordseter=input(Col.BLUE+"enter student password: "+Col.RESET)
                Flag2=False
                for i in range(0,len(Control.listObjs)):
                    if nameset==Control.listObjs[i].getname():
                        print(Col.RED+"This Student is already added"+Col.RESET)
                        Flag2=True
                if Flag2:
                    continue
                newobj=Student(nameset,ageset,idseter,phonenumseter,passwordseter)
                Control.addnewstudent(newobj)
                print(Col.GREEN+"Student added"+Col.RESET)
            elif  option==2:
                studentname=input(Col.BLUE+"Enter the student name you want to remove: "+Col.RESET)
                Control.removestudent(Control(),studentname)
            elif option==3:
                managestudents()
            elif option==4:
                #==================post news page==============
                while True:
                    print(Col.BLUE + "Choose an option:" + Col.RESET)
                    print(Col.BLUE + "Add News =>> 1" + Col.RESET)
                    print(Col.BLUE + "Show Students News =>> 2" + Col.RESET)
                    print(Col.BLUE + "Remove News =>> 3")
                    print(Col.BLUE + "Back window before this =>> 4" + Col.RESET)
                    print(Col.BLUE + "Exit  =>> 0" + Col.RESET)

                    choice = int(digitchecker(input(Col.BLUE + "Enter your option number: " + Col.RESET)))

                    if choice == 1:
                        Control.add_news()
                    elif choice == 2:
                        News.ShowNews()
                    elif choice == 0:
                        exit()
                    elif choice == 3:
                        News_title = input(Col.BLUE + "Enter the Title of the annoucment you want to remove: " + Col.RESET)
                        Control.Remove_news(News_title)
                    elif choice== 4:
                        break
                    else:
                        print(Col.RED + "Invalid choice. Please try again." + Col.RESET)
                #===================post news page================
            elif option==5:
                ManageCourses()
            elif option==6:
                print("\n\n")
                view_complaints()
                print("\n\n")
                while True:
                    print(Col.BLUE+"Remove a Complaint >1"+Col.RESET)
                    print(Col.BLUE+"Back >2"+Col.RESET)
                    anotheroption=int(digitchecker(input(Col.BLUE+"Choose your option:"+Col.RESET)))
                    if anotheroption==1:
                        ComplaintNumber=int(digitchecker(input(Col.BLUE+"Choose Complaint Number To remove:"+Col.RESET)))
                        remove_complaint(ComplaintNumber)
                    elif anotheroption==2:
                        break
                    else:
                        print(Col.RED+"Invalid Option, retry"+Col.RESET)
            else:
                print(Col.RED+"invalid option try again "+Col.RESET)
        if result[1]==2:
            print(Col.GREEN+f"Welcome {result[0].getname()}\n"+Col.RESET)
            print(Col.YELLOW+"========================================="+Col.RESET)
            print(Col.YELLOW+"===============Your Data================="+Col.RESET)
            print(Col.YELLOW+"=========================================\n"+Col.RESET)
            result[0].getfullinfo()
        while result[1]==2:
            Choice=100
            print("\n\n")
            print(Col.BLUE+"Show Annoucments =>> 1"+Col.RESET)
            print(Col.BLUE+"Manage your Courses =>>2"+Col.RESET)
            print(Col.BLUE+"Submit a Complaint =>>3"+Col.RESET)
            print(Col.BLUE+"Edit your Information =>>4"+Col.RESET)
            print(Col.BLUE+"sign out =>>5"+Col.RESET)
            print(Col.BLUE+"Exit =>> 0"+Col.RESET)
            Choice=int(digitchecker(input(Col.BLUE+"Enter your choice: "+Col.RESET)))
            if Choice==1:
                News.ShowNews()
            elif Choice==5:
                break
            elif Choice==2:
                ManageCoursesForStudents(result[0])
            elif Choice==0:
                exit()
            elif Choice==3:
                name = input(Col.BLUE+"Enter your name: "+Col.RESET)
                email = input(Col.BLUE+"Enter your email: "+Col.RESET)
                message = writepargraph()
                submit_complaint(name, email, message, result[0].getid())
            elif Choice==4:
                Student.editinformation(result[0])
                print(Col.YELLOW + "=========================================" + Col.RESET)
                print(Col.YELLOW + "===============Your Data=================" + Col.RESET)
                print(Col.YELLOW + "=========================================\n" + Col.RESET)
                result[0].getfullinfo()
            else:
                print(Col.Red+"invalid input retry"+Col.RESET)


print(Col.BLUE+"============================================================"+Col.RESET)
print(Col.BLUE+"===================Welcome To our Programme================="+Col.RESET)
print(Col.BLUE+"===================Student Managment System================="+Col.RESET)
print(Col.BLUE+"============================================================\n\n"+Col.RESET)

admin1=Control()
main1()

