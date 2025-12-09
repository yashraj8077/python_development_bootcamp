"""
Take an input from the user -> string
Check if pallindrome 
Eg - madam, mam, poop
"""
def pallindromeChecker(pall:str) -> str:
    unreversedStr = pall.lower()
    myStr = list(pall.lower())
    myStr.reverse()
    reversedStr = ''.join(myStr)
    
    if unreversedStr == reversedStr:
        return f'Your string is a pallindrome: {unreversedStr} = {reversedStr}'
    else:
        return f'Your string is not a pallindrome: {unreversedStr} not equal {reversedStr}'


info = """
      Enter word in input or press any of the keys:
      i     : Information
      e     : to exit
"""

print('*/*/*/*/*/*/* WELCOME TO PALLINDROME CHECKER */*/*/*/*/*/*')
print(info)
while True:
    word = input('\nPlease enter your word (press i for help): ')

    if word == 'i':
        print(info)
    elif word == 'e':
        print('Thankyou for using pallindrome checker, have a great day!!')
        break
    else:
        print(pallindromeChecker(word))

