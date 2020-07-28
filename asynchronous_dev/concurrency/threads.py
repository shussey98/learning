import time

#from threading import Thread


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
print(f'Single thread total: , {time.time() - start}')

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    two_start = time.time()
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calc())
        pool.submit(ask_user())


    print(f'Two thread time: {time.time() - two_start}')