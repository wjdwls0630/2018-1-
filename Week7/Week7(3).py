#Loop practice 1

a = [1,2,1,8,9,4,2,5,1,3]
b = []  # The new list to print out

# Add your code here
number=int(input("Enter an integer: "))
for c in a :
	if c<number :
		b.append(c)
print(b)

print("="*60)

#Loop practice 2

a = [1, 1, 2, 3, 5, 8, 13, 24, 34, 55]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
c = []

# Add your code here
for d in a:
    if a.count(d) > 1:
        a.remove(d)
    if d in b:
        c.append(d)

print(c)


print("="*60)

#Guessing number 1
# Use random module
import random
number=random.randrange(1,10)

while True :
    Guess_number = int(input("Guess(1-9) :"))
    if number>Guess_number:
        print("Too low")
    elif number<Guess_number :
        print("Too high")
    else : break
print("Exactily right!")

print("="*60)

#Guessing number 2
#Binary Search
print("Let's start the game!")
ans = 0
a = 0
b = 100
m = (a + b) // 2

while ans != 1:

    print("Is your guess {0}?".format(m))
    ans = int(input("Too Low(0), right answer(1), Too High(2) : "))
    if ans == 0:
        a = m + 1
        m = (a + b) // 2
    elif ans == 2:
        b = m - 1
        m = (a + b) // 2
    else:
        print("Guess is right!")



