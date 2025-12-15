username = input('enter your username: ')

def validation(username):
    if len(username) < 8:
        return False
    elif username == username.capitalize():
        print('your log in.')
    else :
        print('sorry')
validation(username)
        