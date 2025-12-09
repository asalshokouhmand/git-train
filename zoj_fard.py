

def number_type(number):
    if number.isnumeric():
        num = int(number)
        if num % 2 == 0:
            print("your number is even!")
        else:
            print('your number is odd!')
    else :
        print('try again.')
while True:
    num = input('enter your number: ')
    number_type(num)       
     