# name = input('Enter your name: ')
# print(f'Hello, {name}!')

'''
def greet():
    name = input('Enter your name: ')
    print(f'Hello, {name}!')

print('Before the funciton')

greet()

print('After the funciton')
'''

def check_if_prime(n): # number is called a parameter
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

def check_primes(n):
    for n in range(2, n):
        check_if_prime(n)

check_primes(1000*1000)