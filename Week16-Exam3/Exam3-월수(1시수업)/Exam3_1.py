class Item() :
    def __init__(self,id_num="",name="",price=0.0):
        self.id_num=id_num
        self.name=name
        self.price =price
    def __str__(self):
        a="아이디 번호 : {}".format(self.id_num)
        b="이름 : {}".format(self.name)
        c="가격 : {}".format(self.price)
        return a+b+c

    def set_value(self,id_num,name,price):
        self.id_num = id_num
        self.name = name
        self.price = price

    def get_value(self):

        return self.id_num,self.name,self.price

class Coffee(Item) :
    def __init__(self,id_num="",name="",price=0.0,bean=""):
        super().__init__(id_num,name,price)
        self.bean=bean
    def set_value(self,id_num,name,price,bean):
        super().set_value(id_num,name,price)
        self.bean=bean


# do not modify below
item1 = Item("B01","녹차머핀", 4000)
item2 = Item()
item2.set_value("B02","클래식스콘", 4000)

coffee1 = Coffee("C01", "뉴그린티프라푸치노", 5500, "안티구아")
coffee2 = Coffee()
coffee2.set_value("C02", "콜드폼콜드브루", 5500, "예가체프")

print(item1)
print(item2)
print(coffee1)
print(coffee2)
print()
print(item1.get_value())
print(item2.get_value())
print(coffee1.get_value())
print(coffee2.get_value())