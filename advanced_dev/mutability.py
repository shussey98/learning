friends_seen = {
    'Rolf':31,
    'Jen':1,
    'Anne':7
}

#print(id(friends_seen))

friends_seen = {
    'Rolf':31,
    'Jen':1,
    'Anne':7
}

#print(id(friends_seen))

friends_seen['Rolf'] = 0

#print(id(friends_seen))

my_int = 6
#print(id(my_int))
my_int = my_int + 1
#print(id(my_int))

friends = ['Max','Sharleen']
#print(id(friends))
friends.append('Me')
#print(id(friends))

#Argument mutability
friends_seen = {
    'Rolf':31,
    'Jen':1,
    'Anne':7
}

def see_friend(friends, name):
    print(id(friends))
    friends[name]=0

#print(id(friends_seen))
#print(id(friends_seen['Rolf']))
see_friend(friends_seen,'Rolf')
#print(id(friends_seen['Rolf']))
#print(id(friends_seen))

#Default values for params
accounts = {
    'checking':1958.00,
    'savings':3695.50

}

def add_balance(amount:float, name:str = 'checking') -> float:
    accounts[name] += amount
    return accounts[name]

transactions = [
    (-10.0,'checking'),
    (-15.0,'checking'),
    (-10.0,'savings'),
    (-32.0,'checking'),
    (-10.0,'savings'),
    (-11.3,'checking'),

]

#argument unpacking

for t in transactions:
    #add_balance(t[0], t[1])
    add_balance(*t)


from collections import defaultdict


mappings = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def mapper(letter,**kwargs):
    return mappings[kwargs]

print(mapper('a','b'))





