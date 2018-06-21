class Mystudent() :
    def __init__(self, name="no name", exam1=0,exam2=0):
        self.name =name
        self.exam1=exam1
        self.exam2 =exam2

    def total(self):
        return self.exam1+self.exam2



number=int(input())
stu_list=[]
for i in range(number) :

    name=input()
    exam1=int(input())
    exam2=int(input())
    instance = Mystudent(name, exam1, exam2)
    stu_list.append(instance)


for i in range(len(stu_list)) :
    print(stu_list[i].name,stu_list[i].exam1,stu_list[i].exam2,stu_list[i].total())
