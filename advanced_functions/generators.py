def hundred_numbers():
    i=0
    while i<100:
        yield i
        i +=1

#print(hundred_numbers())

g= hundred_numbers()
#print(list(g))

def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2,n):
            if n%x == 0:
                break
        else:
            yield n
g = prime_generator(100)
#generator classes and iterators

# An iterato

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number<100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
    def __iter__(self):
        return self

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

##print(list(FirstHundredIterable()))

my_gen = FirstHundredGenerator()
#print(my_gen)


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()

g= FirstFiveIterator()
#print(next(g))


class AnotherIterable:
    def __init__(self):
        self.cars = ['Ford','Polo']

    def __len__(self):
        return len(self.cars)
## indexing must have getitem
    def __getitem__(self, i):
        return self.cars[i]

#filter takes in a function and a iterable
def start_with_a(friends):
    return friends.startswith('A')

friend = ['Andy','Andrew','Max']
#starts_with_a = filter(start_with_a, friend)
starts_with_a = filter(lambda friends: friends.startswith('A'), friend)

generator_friend = (f for f in friend if f.startswith('A'))

print(next(generator_friend))

#map

friends_lower = map(lambda x: x.lower(),friend)
lower_gen = (f.lower() for f in friend)
print(next(lower_gen))















