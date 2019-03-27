class Student: 
    def __init__(self, name, age, standard):
        self.name = name
        self.age = age
        self.standard = standard

    def checkMyAge(self):
        print("My age is: " + str(self.age))

    def checkMyName(self):
        print("My name is: " + self.name)
        
    def checkMyStandard(self):
        print("My standard is: " + str(self.standard))   

    def fixMyName(self):
        self.name = self.name.upper()

    def MyStandard(self):
        if  self.standard < 5 and self.standard> 0:
            print("I am in nursary school")
        elif self.standard > 10:
            print("I am in primary school")

        elif self.standard < 10:
            print("I am in primary school")
            
        elif self.standard <= 18:
            print("I am in high school")
        else:
            print("I must not in school")


#Main
myFirstStudent = Student("gill",16,10)
mySecondStudent = Student("deep",12,7)
myThirdStudent = Student("prabh",10,5)
myFourthStudent = Student("jot",7,3)
myFifthStudent = Student("aman",11,6)
mySixthStudent = Student("sandeep",10,6)
mySeventhStudent = Student("moto",9,5)
myEighthStudent =Student("mann",15,9)
myNinethStudent = Student("harpreet",6,2)
myTenthStudent = Student("preet",8,4)

myListOfPeople = [myFirstStudent, mySecondStudent, myThirdStudent, myFourthStudent, myFifthStudent, mySixthStudent, mySeventhStudent, myEighthStudent, myNinethStudent   ]
myListOfPeople.append(myTenthStudent)

print(myFirstStudent.name + ", " + mySecondStudent.name + ", " + myThirdStudent.name + ", " + myFourthStudent.name + ", " + myFifthStudent.name + ", " + mySixthStudent.name + ", " + mySeventhStudent.name + ", " + myEighthStudent.name + ", " + myNinethStudent.name + ", " + myTenthStudent.name )

for student in myListOfPeople:
    student.checkMyAge()
    student.checkMyName()
    student.checkMyStandard()
    student.fixMyName()
    student.checkMyName()
    student.MyStandard()
