class employee:
    print("one")
    def __init__(self,eno,ename,esal):
        print("two")
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def dis(self):
        print("three")
        print("employee name",self.ename)
        print("employee sal ",self.esal)
#emp=employee(2,"test",400)
#emp.dis()
class manager:
    def update(emp):
        emp.esal=emp.esal+1
        emp.dis()
emp=employee(1,'durga',2000)
manager.update(emp)



