#solution a

#파일을 연다
file = open('text.txt','r')

#헤더 부분을 제거한다.
data = file.readline()
data = file.readline()

while data.startswith('#'):
    data = file.readline()
#이 시점에서 data는 red 5
data = data.strip().split() #띄어쓰기 부분을 기준으로 데이터에 입력
#이 시점에서 data = [red , 5]

#데이터를 딕셔너리에 저장한다.
dict_bird = {data[0]: int(data[1])}
#이 시점에서 dict_bird = {red : 5}
for data in file:
    data = data.strip().split()
    if data[0] in dict_bird:
        dict_bird[data[0]] = dict_bird[data[0]]+int(data[1])
    else:
        dict_bird[data[0]] = int(data[1])

#딕셔너리의 key부분을 정렬(list)
list_bird = list(dict_bird.keys())
list_bird.sort()
#정렬 순서대로 화면에 출력
for l in list_bird:
    print(l,dict_bird[l])

file.close()

print('='*60)
#solutino b

file=open('text.txt','r')
#header
file.readline()

lines=file.readlines()
#skip "#"
data=[]
for line in lines :
    if not line.startswith("#") :
        data.append(line)


data_dict=dict()
for element in data :
    key,value=element.split()
    if key in data_dict :
        data_dict[key]=int(data_dict[key])+int(value)

    else :
        data_dict[key]=value


sort_data_dict=list(data_dict.keys())
sort_data_dict.sort()
for i in sort_data_dict :
    print(i,data_dict[i])

file.close()

print('='*60)