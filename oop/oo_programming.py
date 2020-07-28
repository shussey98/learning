my_student = {
    'name':'Rolf',
    'grades':[70,88,90,99]
}

def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

# Creating Classes

class Student:
    def __init__(self, new_name,new_grade):
        #self is a blank object , name is a variable
        self.name = new_name
        self.grades=new_grade

    def average(self):
        return sum(self.grades)/len(self.grades)

student_one = Student('Rolf Smith',[70,88,90])

#print(student_one.average())
#print(Student.average(student_one))

class Movie:
    def __init__(self, name, year):
        self.name=name
        self.year=year
#print(Movie('the matrix',1994).name)

#Magic Methods
class Student:
    def __init__(self,name):
        self.name=name

movies = ['Matrix','Nemo']
print(movies.__class__)

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self,i):
        return self.cars[i]
    def __repr__(self):
        return f'<Garage {self.cars}>'
    def __str__(self):
        return f'Garage with {len(self)} cars'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
#print(repr(ford))
#print(ford)

## Inheritance

class Students:
    def __init__(self, name, school):
        self.name = name
        self.school=school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Students):
    def __init__(self, name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary*37.5

rolf  = WorkingStudent('Rolf','MIT',15.50)

#print(rolf.weekly_salary)

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object=Foo()
#my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parmas')
another_object = Bar()
#another_object.hi()

class FixedFloat:
    def __init__(self, amount):
        self.amount=amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, val1,val2):
        return cls(val1 + val2)

number = FixedFloat(18.5748)
new_num = FixedFloat.from_sum(10.8484,4.82828)
print(new_num)

class Dollar(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'<Dollar {self.symbol}{self.amount:.2f}>'
money = Dollar.from_sum(19,6.342)
print(money)
















