#if-else Practice
print("="*60)

number=int(input("Enter a number: "))
if number%2==0:
    print("You picked an even number")
else :
    print("You picked an odd number")

print("="*60)

#if-elif-else Practice
First_number=int(input("Input one number: "))
Second_number=int(input("Input another number: "))
if First_number>Second_number:
    print(First_number,"is larger than",Second_number)
elif First_number==Second_number:
    print(First_number, "is equal to", Second_number)
else :
    print(First_number, "is smaller than", Second_number)

print("="*60)

#GPA Problem 1 Solution A
def get_score(grade):
	if grade =="A":
		score=4.0
	elif grade == "B":
		score=3.0
	elif grade == "C":
		score=2.0
	elif grade == "D":
		score=1.0
	else :
		score=0.0
	return score
English_grade=input("What\'s the grade for English? ")
Physics_grade=input("What\'s the grade for Physics? ")
Programming_grade=input("What\'s the grade for Programming? ")


GPA=(get_score(English_grade)+get_score(Programming_grade)+get_score(Physics_grade))/3
print("GPA is",round(GPA,2))

print("="*60)

#GPA Problem 1 Solution B
English_grade=input("What\'s the grade for English? ")
Physics_grade=input("What\'s the grade for Physics? ")
Programming_grade=input("What\'s the grade for Programming? ")
list_grade=[English_grade,Physics_grade,Programming_grade]
sum=0
for i in list_grade :
    if i == "A" :
        i = 4.0
    elif i == "B":
        i = 3.0
    elif i == "C":
        i = 2.0
    elif i == "D":
        i = 1.0
    else:
        i = 0.0
    sum=sum+i

print("GPA is",round(sum/3 ,2))

print("="*60)

#GPA Proble 1 Solution C
grade_score={"A" : 4.0 ,"B" : 3.0, "C" : 2.0, "D" : 1.0, "F" : 0.0}
English_grade=input("What\'s the grade for English? ")
Physics_grade=input("What\'s the grade for Physics? ")
Programming_grade=input("What\'s the grade for Programming? ")
GPA=(grade_score.get(English_grade)+grade_score.get(Physics_grade)+grade_score.get(Programming_grade))/3
print("GPA is",round(GPA ,2))

print("="*60)