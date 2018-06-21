
file_name =input("Enter the filename: ")
def find(file_name) :
    file =open(file_name ,'r')
    
    lines=file.readlines()
    data=[]
    for line in lines :
        if not line.startswith("#"):
            data.append(line.strip())
    file.close()
    return data
def make_list(data):
    bird_list=[]
    value_list=[]
    for element in data :
        name,number = element.split()

        bird_list.append(name)


def make_dict(data):
    bird_dict=dict()
    for element in data :
        name,number=element.split()
        bird_dict[name]=int(bird_dict.get(name,0))+int(number)

    return bird_dict
	
bird_dict=make_dict(find(file_name))

bird_list=list(bird_dict.keys())
value_list=list(bird_dict.values())

bird_dict_reverse=dict()
for i in range(len(value_list)) :
    bird_dict_reverse[value_list[i]]=bird_list[i]

value_list.sort(reverse=True)

for i in value_list :
    print(bird_dict_reverse[i],i)



















