from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

temps = [13,14,14,16,17]
temp_counter = Counter(temps)
#print(temp_counter[14])

workers = [('Mat','MIT'),('Sam','LSE'),('Bob','Oxford'),('Bob','MIT'),]

# defaultdict is initialized by a function
worker_dict = defaultdict(list)
for name, uni in workers:
    worker_dict[name].append(uni)

#print(worker_dict)

#Ordered Dict
o = OrderedDict()
o['Rod'] = 6
o['Sam'] = 4
o['Jen'] = 10

#print(o)

o.move_to_end('Rod')
#move to start
o.move_to_end('Jen',last=False)
#print(o)
o.popitem()
#print(o)

##Named Tuple

account_x = ('checking',20.30)
Account = namedtuple('Account',['name','amount'])
account = Account('checking',18.50)
#print(account)

accountNamedTuple = Account(*account_x)
#print(accountNamedTuple)
#print(accountNamedTuple._asdict())

#Deque - double ended queue

friends = deque(('Rolf','Charles','Jen','Max'))
friends.append(friends[0])
#friends.appendleft('Bob')
#print(friends)
#friends.pop()
friends.popleft()
#print(friends)



