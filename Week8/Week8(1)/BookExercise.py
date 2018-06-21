#10.10Exercise 풀이

print('='*60)

#os모듈로 현재 디렉터리 확인
import os
print(os.getcwd())

print('='*60)

#1 solution백업 파일을 만들기 파일명 맨 뒤에 .bak 을 넣어서 만들 면 된다

#2 solution

file= open('alkaine_metals.txt','r')
list_atom=[]
for line in file :
    a=line.split()
    list_atom.append(a)

file.close()
print(list_atom)

print('='*60)

#3 solution
#모든 문자열 거꾸로 읽기
file= open('alkaine_metals.txt','r')
content1=file.read()
print(content1[::-1])
file.close()

print('='*60)

#문장 을 역순으로 읽기

file= open('alkaine_metals.txt','r')
content2=file.readlines()
for line in reversed(content2) :
    print(line.strip())
file.close()

print('='*60)

#4 lynx파일 읽자

#time_series 참고 skip_header는 그대로 하고 process_file을 재정의해서 lynx 파일의 데이터를 한번에 다 읽자
def skip_header(reader):
    """ (file open for reading) -> str
    Skip the header in reader and return the first real piece of data.
    """
    # Read the description line
    line = reader.readline()
    # Find the first non-comment line
    line = reader.readline()  # 초기값 설정
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the first real piece of data
    return line

def process_file(reader):
    """ (file open for reading) -> NoneType
    Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a
    sequence of data.
    """
    # Find and print the first piece of data
    line = skip_header(reader).strip()
    print(line)

    # Read the rest of the data
    a=reader.read()
    return a

file=open('lynx.txt','r')

print(process_file(file))

file.close()

print('='*60)

#11.8 Exercise

#1 solution
a=[1,2,3,4,5,4,21,2,31,1,21,3,12,31,12,3,4,5,6,7,6]
def find_dups(L) :
    set_list=set(L)
    return set_list

print(find_dups(a))

print('='*60)

#2 solution

def mating_pairs(males, females):
    pairs = set()
    for a in range(len(males)):
        element = males.pop(), females.pop()
        pairs.add(element)

    return pairs


males = input("input males : ")  # ex) m1 m2 m3 m4
females = input("input females : ")  # ex) f1 f2 f3 f4
males_set = set(males.split())
females_set = set(females.split())
pairs = mating_pairs(males_set, females_set)
print(pairs)
# ex) {('m3', 'f3'), ('m1', 'f1'), ('m4', 'f4'), ('m2', 'f2')}

print("="*60)

#3 solution

def get_the_name(file) :
    file_name=open(file,'r')
    first=file_name.readline()
    author, name = first.split()
    file_name.close()
    return name

def all_author_name(L) :
    result=set()
    for i in L :
        name=get_the_name(i)
        result.add(name)

    return result


files=input("input file name : ")#1.pdb 2.pdb 3.pdb
list_file=files.split()
print(all_author_name(list_file))

print("="*60)

#4 solution

def count_values(dictionary):
	# add your code here
	value_count=set(dictionary.values())
	num=len(list(value_count))
	return num


a = dict()
keys = input("key 값을 입력 :").split()
values = input("value 값을 입력").split()
for i in range(len(keys)):
	a[keys[i]] = values[i]

print(count_values(a))

print("="*60)

#5 solution

subatomic_particles={"neutron" : 0.55, "proton" : 0.21, "meson" : 0.03, "muon": 0.07, "neutrino" : 0.14}
def get_least_subatiomic(dictionary) :
    name_list=list(dictionary.keys())
    value_list=list(dictionary.values())
    least=min(value_list)
    index=value_list.index(least)
    return name_list[index]

print(get_least_subatiomic(subatomic_particles))

print("="*60)

#6 solution 미완성
example={"a":1, "b":1, "c":2,"d":2,"e":3}
def count_duplicates(dictionary) :
    value_list=list(dictionary.values())
    count=0
    for key in dictionary.keys() :
        if value_list.count(dictionary[key])>1 :
            count=count+1

    return count

print(count_duplicates(example))

print("="*60)

# 7solution
keys = ["R", "G", "B"]
values = input("값을 입력 : ").split()
color = dict(zip(keys, values))
def is_balanced(dictionary):
    values=list(dictionary.values())

    for value in values :
        print(value)
        value_float=float(value)
        if value_float>1 :
            values.remove(value)


    return len(list(dictionary.values())) == len(values)

print(is_balanced(color))

print("="*60)

#8solution 미완성

#def dict_intersect(first_dict, second_dict) :

#9 solution

DataBase={
    'jgoodall' : {'suranme' : "Goodall",
                  'forename' : 'Jane',
                  'born' : 1934,
                  'died' : None,
                  'notes' : 'primate researcher',
                  'author' : ['In the shadow of Man',
                              'The Chimpanzees of Gombe']},


    'rfranklin' : {'suranme' : "Franklin",
                   'forename' : 'Rosalind',
                   'born' : 1920,
                   'died' : 1957,
                   'notes' : 'contributed to discovery of DNA'},

    'rcarson' : {'suranme' : "Carson",
                 'forename' : 'Rachel',
                 'born' : 1907,
                 'died' : 1964,
                 'notes' : 'raised awareness of effects of DDT',
                 'author' : ['Silent Spring']}

}

def db_headings(DB) :
    fields=DB.values()
    head=set()
    for field in fields :
        items=field.keys()
        for item in items :
            head.add(item)

    return head

print(db_headings(DataBase))

print("="*60)

#10 solution

def db_consistent(DB) :
    fields=list(DB.values())
    items_default=list(fields[0].keys())
    for field in fields :
        print(count)
        items=list(field.keys())
        if items_default != items :
            return False
    return True

print(db_consistent(DataBase))

print("="*60)

#11 solution
vector=[1,0,0,0,0,0,3,0,0,0]

def convert(vector_list) :
    vector_dict={}
    for i in range(len(vector_list)) :
        if vector_list[i]>0 :
            vector_dict[i]=vector_list[i]
    return vector_dict

print(convert(vector))

#11-a

vector_a=[1,2,3]
vector_b=[4,5,6]

def sparse_add(vector1, vector2) :
    vector3=[]
    for i in range(len(vector1)) :
        vector3.append(vector1[i]+vector2[i])
    vector_dict=convert(vector3)
    return vector_dict

print(sparse_add(vector_a,vector_b))

#11-b
def sparse_dot(vector1,vector2) :
    total=0
    for i in range(len(vector1)) :
        total=total+vector1[i]*vector2[i]

    return total

print(sparse_dot(vector_a,vector_b))

#11-c

def sparse_len(vector1,vector2) :
    from math import sqrt
    diff_total=0
    for i in range(len(vector1)) :
        diff_total=diff_total+abs(vector1[i]-vector2[i])**2

    return round(sqrt(diff_total),5)

print(sparse_len(vector_a,vector_b))
