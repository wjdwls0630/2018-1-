# class student
print("="*60)

class Student:
    name = ""
    id = 0
    gender = ""


a = Student()
b = Student()
c = Student()
a.name = "P"
a.id = 32
a.gender = "male"
print(a.name, a.id, a.gender)

print("="*60)

#class Book

class Book:
	def __init__(self, title, authors, publisher ,ISBN, price) :
		self. title=title
		self .authors=authors[:]
		self.publisher=publisher
		self . ISBN=ISBN
		self. price=price
	def num_authors(self) :
		return len(self.authors)
	def __str__(self) :
		details=" title : {0}\n authors : {1}\n Publisher : {2}\n ISBN : {3}\n Price : {4}"
		.format(self.title,self.authors,self.publisher,self.ISBN,self.price)
	def __eq__(self,other) :
		return self.ISBN==other.ISBN

print("="*60)

#class member

class Member:
	def __init__ (self, name, address, email) :
		self.name=name
		self.address=address
		self.email=email
	def __str__ (self) :
		details="Name : {0}\nAddress : {1}\nEmail : {2}".format(self.name,self.address,self.email)
		return details
class Faculty(Member) :
	def __init__(self,name,address,email,faculty_num) :
		super().__init__(name,address,email)
		self.faculty_num=faculty_num
		self.courses_teaching=[]
	def __str__ (self) :
		member_string=super().__str__()
		details="{0}\nFaculty_Num : {1}\nCourses_teaching : {2}".format(member_string, self. faculty_num,self.courses_teaching)
		return details
class Student(Member):
	def __init__(self,name,address,email,student_num) :
		super().__init__(name,address,email)
		self.course_taken=[]
		self.course_taking=[]

a=Faculty("a","d",1,2)
b=Student("b","j","k",4)

print("="*60)

print(a)

print("="*60)

print(b)