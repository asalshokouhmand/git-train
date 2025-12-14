# cs = [
#     {
        
#     }
# ]










class User :
    def __init__(self, name, lastname):
        self.fname = name
        self.lname = lastname
    def fullname(self):
        print(f'my name is {self.fname} {self.lname}')
        
# u1 = User('asal' , 'shokouhmand')
# u1.fullname()

class Student(User):
    def __init__(self, name, lastname , email):
        super().__init__(name, lastname)
        self.email = email
    def fullname(self):
        print('im an student')
        super().fullname()

# s1 = Student('asal','asa','a@h')
# s1.fullname()
# s1 = Student('asal','shk','asal@')
# s1.fullname()
class Teacher(User):
    def __init__(self, name, lastname , code):
        super().__init__(name, lastname)
        self.code = code
    def fullname(self):
        print('i am a teacher.')
        super().fullname()
        
t1 = Teacher('ali','ahmadi',1234)
s1 = Student('asal','shk','asal@')
t1.fullname()
print("-----------")
s1.fullname()