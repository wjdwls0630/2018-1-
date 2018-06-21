class Unit() :
    def __init__(self,id="",name="",hp=0):
        self.id=id
        self.name=name
        self.hp=hp

    def __str__(self):
        a="ID:{}, ".format(self.id)
        b="Name: {}, ".format(self.name)
        c="HP: {}".format(self.hp)
        return a+b+c

    def set_value(self,id,name,hp):
        self.id = id
        self.name = name
        self.hp = hp

    def get_value(self):
        return self.id, self.name, self.hp

class Hero(Unit) :
    def __init__(self,id="",name="",hp=0,spells=[]):
        super().__init__(id,name,hp)
        self.spells=spells[:]

    def __str__(self):
        a=super().__str__()
        b=", "
        c="Spells:{}".format(self.spells)
        return a+b+c
    def set_value(self,id,name,hp,spells):
        super().set_value(id,name,hp)
        self.spells=spells[:]

    def get_value(self):
        return self.id, self.name, self.hp, self.spells

# do not modify below
unit1 = Unit("U01","외각포탑", 3800)
unit2 = Unit()
unit2.set_value("U02","내부포탑", 3600)

hero1 = Hero("H01", "마스터이", 2162, ["강타", "점멸"])
hero2 = Hero()
hero2.set_value("H02", "이즈리얼", 1946, ["순간이동", "점멸"])

print(unit1.get_value())
print(unit2.get_value())
print(hero1.get_value())
print(hero2.get_value())
print()
print(unit1)
print(unit2)
print(hero1)
print(hero2)