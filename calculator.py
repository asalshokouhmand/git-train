
def calculator(a,b):
    
    def sum(a , b):
        return a + b
    # return sum(a,b)
    def minese(a,b):
        return a-b
    def devide(a,b):
        return a / b
    def zarb(a,b):
        return a*b
    
    if operation == '+':
        return sum(a,b)
    if operation == '-':
        return minese(a,b)
    elif operation == '/':
        return devide(a,b)
    elif operation == '*':
        return zarb(a,b)
    

num1 = float(input('enter the number:'))
operation = input('choose ( + , - , / , *):')
num2 = float(input('enter the number:'))

result = calculator(num1 ,num2)

print(result)