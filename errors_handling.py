
#Traceback - where the error happened
#NameError : name '' is not defined
#IndexError: list index out of range
#KeyError: No key in dictionary / incorrectly used
#AttributeError: list object has no attribute - not defined in self/ def
#NotImplementedError: raise this error when you haven't implented yet
#RunTimeError: maxed out time
#SyntaxError: missed colon / '' ...
#IndentationError: not correctly blocked
#TabError: Use 4 spaces instead of tab
#TypeError: unsupported operand type i.e 'int' + 'str'
#ValueError: invalid int('20.5') instead of float('20.5')
#ImportError: circular import with modules
#DeprecationWarning: no longer best way of doing something

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}'





class Garage:
    def __init__(self):
        self.cars= []

    def __len__(self):
        return len(self.cars)
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'{car.__class__.__name__} is not a Car object')
        self.cars.append(car)

ford=Garage()

fiesta = Car('Ford','Fiesta')

try:
    ford.add_car('fiesta')
except TypeError:
    print('Your car is not a Car')
finally:
    print(f'Then garage didn\'t take your item')

class MyCustomError(TypeError):
    """
    Exception raised when error code is needed.
    """
    def __init__(self, message,code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


err = MyCustomError('Something happened',500)
#print(err.__doc__)

def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square=n**2
        return n_square
    except ValueError:
        print('Your input is invalid. 0')
        return 0

print(power_of_two())
print(power_of_two())