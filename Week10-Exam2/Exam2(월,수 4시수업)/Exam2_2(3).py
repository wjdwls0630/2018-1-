
file_name =input("Enter the filename: ")
def find(file_name) :
    file =open(file_name ,'r')
    file.readline()
    lines=file.readlines()
    data=[]
    for line in lines :
        if not line.startswith("#"):
            data.append(line.strip())
    return data

def search(data):
    number_list=[]

    for element in data :
        if not element.startswith('-') :
            number_list.append(int(element))
    number_list.sort(reverse=True)
    largest1=number_list[0]
    largest2=number_list[1]
    largest1_index=data.index(str(largest1))
    largest2_index=data.index(str(largest2))
    return largest1_index, largest2_index

print(search(find(file_name)))















