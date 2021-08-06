class Employee:
    def __init__(self):             #constructor
        self.name = input("Enter the name")
        self.age = input("Enter the age")

    def display(self):              #non-static method
        print("Name: ",self.name)
        print("Age: ",self.age)

    @staticmethod                   #Static method is assigned to the class not to the object
    def isWorking(name):
        print(name, "is working")

    @classmethod
    def isAgetoRetire(Employee):
        age = int(input("Enter Age 2: "))
        if age >= 60:
            print("Age to retire")
        else:
            print("Age to work")

obj = Employee()
obj.display()

Employee.isWorking("Rajesh")
Employee.isAgetoRetire()



#legacy of class method
class human:
    age = 20

    def getAge(human):
        print(human.age)

human.getAge = classmethod(human.getAge)
human.getAge()
