class student:
    def __init__(self,name,no,marks):

       self.name = name
       self.no = no
       self.marks = marks
       print('name',name)



    def talk(self):
        print('my name is',self.name)
        print('my no is ', self.no)
        print('my marks are',self.marks)
s1=student('sunny',1,50)
s2=student('bunny',2,40)
s1.talk()
s2.talk()

