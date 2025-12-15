def fibonacci(n):
    a , b = 0 , 1
    result = []
    
    for item in range(n):
        result.append(a)
        a , b = b , a+b
        
    return result
n = int(input("enter the number: "))
numbers = fibonacci(n)

print(numbers)

