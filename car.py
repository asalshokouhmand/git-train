class Car :
    
    cars_number = 0
    
    def __init__(self , name , price):
        self.name = name
        self.price = price
        self.status = False
        Car.cars_number += 1
    def start(self):
        if self.status == False:
            self.status = True
            print(f'{self.name} is starting.')
        else:
            print('im on :/ ')
        
    def off(self):
        if self.status:
            self.status = False
            print(f'{self.name} is off.')
        else:
            print('start first')
        
# name = input('enter the name of your car: ')
# price = input('how much is it? ')

c1 = Car("benz" , 125)

c2 = Car("bmw" , 130)

# c1.start()
# c1.start()
# c1.off()
# c1.off()
print(c2.name)

# c2.name = "pride"
# print(c2.name)