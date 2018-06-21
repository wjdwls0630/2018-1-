class Rect() :
    def __init__(self,width=0.0, height=0.0):
        self.width=width
        self.height=height
    def __str__(self):

        return "(width: {},height: {}, area: {})".format(self.width, self.height, round(self.width*self.height,3))
    def __eq__(self, other):
        return (self.width==other.width) and (self.height==other.height)


# do not modify below
rect1_width = float(input())     #input: width
rect1_height = float(input())     #input:height

r1 = Rect(rect1_width, rect1_height)
r2 = Rect()

print("Rect1 =", r1)
print("Rect2 =", r2)
print(r1 == r2)

