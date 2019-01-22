def i_return():
    return 5 + 5

def i_print():
    print(5 + 5)

result = i_return() # this is 10
# another = i_print()

print(f'Result is {result}')
# print(f'Another is {another}')

def fives():
    addtion = 5 + 5
    print(addtion)
    return addtion

result = fives()
print(result)
# print(addtion) -> variables inside the function don't work outside the function