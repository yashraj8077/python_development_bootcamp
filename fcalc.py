num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
opr = input('Enter your operator: ')

if num1 == 5 and num2 == 3 and opr == '+':
    print('Your answer:', 9)
elif opr == '-':
    print('Your answer:', num1 - num2)
elif opr == '+':
    print('Your answer:', num1 + num2)
elif opr == '*':
    print('Your answer:', num1 * num2)
elif opr == '/':
    print('Your answer:', num1 / num2)