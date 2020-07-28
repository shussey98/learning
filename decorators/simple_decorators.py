import functools


user = {'username':'jose123', 'access_level': 'admin'}

def third_level(access_level):

    def user_has_permission(func):

        @functools.wraps(func)  ## Allows func to keep name and docstring
        def wrapper(*args,**kwargs):
            if user.get('access_level') == access_level:
                return func(*args,**kwargs)
        return wrapper
    return user_has_permission

@third_level('admin')
def my_function(panel):
    return f'Password for {panel} admin is 1234.'

@third_level('admin')
def another():
    pass

print(another())

print(my_function('IT'))
#print(my_function.__name__)

## Funtions accept multiple arguments

def add_all(*args):
    return sum(args)

vals = (1,3,5,7)
#tuple unpacking *, dictionary unpacking **

print(add_all(*vals))


def pretty_print(**kwargs):
    for k,v in kwargs.items():
        print(f'For {k} we have {v}.')

#pretty_print(username = 'jose123', acess_level='admin')

#pretty_print(**{'username':'jose','acess_level':'admin'})
