# def hello (name_1 , name_2):
#     print(f'hi {name_1}')
#     print(f'hi {name_2}')
    
# hello('asal' , 'ali')
# ---------------------------------

# def hello(*names):
#     for name in names:
#         print(f'hi {name}')
        
# hello('asal','ali','abbas')
# ---------------------------------

# def me(lname , my_name= 'asal'):
#     print(f'hi {my_name} {lname}')
    
# me(lname='shk')
# ------------------------------------

# def hello(b):
#     for item in b:
#         print(f'hello {item}')
        
# my_list = ['asal','ali']
# hello(my_list)

# hello('asal')
# ---------------------------------------
def calculater(a,b):
    
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

result = calculater(num1 ,num2)

# print(result)