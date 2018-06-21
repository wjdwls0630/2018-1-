#String method
name="jungjin"
print(name.capitalize())
print(str.capitalize(name))
print(name.upper())
print(str.upper(name))
print(len(name))
print(name.count("g"))

#String methond find
name="tomato"
print(name.isalpha())
help(str.find)
print(str.find(name,"o"))
print(name.find('o'))
print(name.find('o',str.find(name,"o")+1))
print(str.find(name,'o',str.find(name,"o")+1))
print(name.find("o",name.find('o',str.find(name,"o")+1)+1))
print(name.find('p'))
print(name.count("e"))

#Hangman game 1
name=input()
character=input()
print("="*30)
print(str.center("Hangman Game",30))
print("="*30)
print("Enter a long word:",end=" ")
print("Enter a character:",end= " ")
if character in name :
	print("{0} is in {1} ({2} times)".format(character, name, name.count(character)))
else : 	print("{0} is not in {1}".format(character, name))


#List method 1
kingdoms=['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[0])
print(kingdoms[len(kingdoms)-1])
print(kingdoms[0:3])
print(kingdoms[2:5])
print(kingdoms[4:])
print(kingdoms[0:0])

#List method 2
ids=[4353,2314,2956,3382,9362,3900]
ids.remove(3382)
print(ids)
print(ids.index(9362))
ids.insert(4,4499)
print(ids)
ids.extend([5566,1830])
print(ids)
ids.reverse()
print(ids)
ids.sort()
print(ids)