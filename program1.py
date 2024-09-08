def get_number(prompt):
    number = input(prompt)
    return number

numberToSquare = int(get_number('Please insert a number: '))
newNumber = pow(numberToSquare, 2)

print('The square is %d' % (newNumber))