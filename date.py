

def convertor(day , month , year):
    if 10<month :
        birthday = year + 622
    # else :
    #     print("try again")
    elif day > 10 and month == 10 :
        birthday = year + 622
    else :
        birthday = year + 621
        
    print(f'your birthday is in {birthday}')
while True:    
    day = int(input('enter the day of your birthday: '))
    month = int(input('enter the month of your birthday: '))
    year = int(input("enter the year of your birthday: "))
    convertor(day , month , year)
        