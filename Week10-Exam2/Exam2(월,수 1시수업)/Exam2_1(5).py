class SmartPhone() :
    def __init__(self,maker="",model="",spec=[],price=0.0):
        self.maker=maker
        self.model=model
        self.spec=spec[:]
        self.price=price

    def setInfo(self,maker,model,spec,price):
        self.maker=maker
        self.model=model
        self.spec=spec[:]
        self.price=price

    def __str__(self):
        a= "Maker: {}\n".format(self.maker)
        b= "Model: {}\n".format(self.model)
        c= "Spec:\n"
        d=""
        for i in self.spec :
            line="\t"+i+"\n"
            d=d+line
        print()
        e="Price: {}".format(self.price)
        return a+b+c+d+e

    def addSpec(self,spec=[]):
        self.spec.extend(spec) #or self.spec=self.spec+spec



s9=SmartPhone("Samsung","Galaxy S9", [], 100)
ix=SmartPhone()
print("-"*10)
print(ix)
print("-"*10)
ix.setInfo("Apple","iPhone X", [], 150)
print("-"*10)
print(s9)
print("-"*10)
print(ix)
print("-"*10)

s9.addSpec(["Super Slow-mo", "AR Emoji Stickers"])
s9.addSpec()
ix.addSpec(["notch","Face ID"])
ix.addSpec(["Dual camera"])
s9.addSpec(["Iris scanner", "Fingerprint"])
print("-"*10)
print(s9)
print("-"*10)
print(ix)
print("-"*10)




