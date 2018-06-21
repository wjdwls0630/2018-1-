a = input('Enter the filename: ')
file = open(a,'r')

bird_dict = {}
for line in file:
	bird = line.strip()
	if bird in bird_dict:
		bird_dict[bird] = bird_dict[bird] + 1
	else:
		bird_dict[bird] = 1
file.close()

list_bird = list(bird_dict.keys())
list_bird.sort()
for i in list_bird:
		print(i,bird_dict[i])
value_bird = list(bird_dict.values())
value_bird.sort()
