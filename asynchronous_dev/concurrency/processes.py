import time
from multiprocessing import Process
#When you need processes to run at the same time (not for waiting)

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')

def complex_calc():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(10000000)]
    print(f'complex_calc, {time.time() - start}')

start = time.time()
ask_user()
complex_calc()

#Processes

if __name__ == "__main__":
    process = Process(target=complex_calc())
    process2=Process(target=complex_calc())
    process.start()
    process2.start()

    start = time.time()
    ask_user()
    process.join()
    process2.join()


    print(f'Single thread total: , {time.time() - start}')