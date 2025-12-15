

def myfunc(name):
    
    ups = 0
    low = 0
    for n in name:
        if n.isupper():
            ups += 1
        elif n.islower():
            low += 1
        else :
            pass

    print(f"upper cases: {ups}")
    print(f"lower cases: {low}")
while True:
    name = input("enter your name: ")
    myfunc(name)
    