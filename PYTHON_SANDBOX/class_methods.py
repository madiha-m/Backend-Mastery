# Create Obj and Create method based on this obj.

class Person:
    # create a new person
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def name_of_person(self):
        print(f'Hi person name is {self.fname} {self.lname}')


# create an obj
personObj = Person("madiha", "Muhammad")
personObj.name_of_person()
