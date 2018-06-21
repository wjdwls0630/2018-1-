#Read a text file

print("="*60)

# Open a text file
file=open("file_example.txt","r")
# read the file
line=file.read()
# close the file
file.close()
# print the contents
print(line)

print("="*60)

#Readlines
# open the file
file=open("planets.txt","r")
# readlines
lines=file.readlines()
# close the file
file.close()
# print the first line of text
first=lines[0]
print(first)
# print its length
print(len(first))
# print the first line of text without \n
print(first.strip())
# print its length
print(len(first.strip()))

print("="*60)

#for line in file
# open the file
file=open("data/planets.txt","r")
# for line in file:
for line in file :
# print the length of each line
    print(len(line.strip()))
# close the file
file.close()

print("="*60)

#Total pelts
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

data_hopedale_file = open("hopedale.txt", "r")
header = data_hopedale_file.readline()
lines = data_hopedale_file.readlines()
data = []
for line in lines:
    if line.startswith("#"):
        lines.remove(line)
    else:
        data.append(line.strip())
data_hopedale_file.close()

total = 0
for element in data:
    total = total + int(element)

print(total)