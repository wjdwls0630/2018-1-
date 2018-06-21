
import os
print(os.getcwd())


"""
일반적인 파일 열고 읽고 닫는 코드
"""

print("="*60)

file=open("file_example1.txt","r")
contents=file.read()
print(contents)
file.close()

print("="*60)

"""with 오픈(파일명 , 모드) as 파일을 담을 변수 를 쓰면 파일을 열고 닫을 필요가 없다"""
with open("file_example1.txt","r") as file:
    contents=file.read()
print(contents)

print("="*60)

"""파일의 디렉토리(절대) 경로를 이용하여 파일을 여는 형식"""


"""OS모듈을 사용하면 터미널을 이용하지 않아도 현재 자신이 위치해있는 경로를 볼수 있고 또 지금 자신이 위치하고 있는 위치에서 다른 위치로 변경할 수 있다."""
import os
print(os.getcwd())#자신의 디렉터리 위치를 리턴 받는다.
#os.chdir(path)#현재디렉터리의 위치를 path값으로 변경한다.

print("="*60)
"""상대 경로 /  : 하위 디렉토리  ../ 상위 디렉토리 , 현재 디렉토리 안에서는 따로 작성하지 않아도 파일을 열 수 있다."""

"""read, readline, readlines의 리턴값의 타입"""

file=open('file_example1.txt',"r")
contents=file.read()
print(type(contents))
file.close()

print("="*60)

file=open('file_example1.txt',"r")
contents=file.readline()
print(type(contents))
file.close()

print("="*60)

file=open('file_example1.txt',"r")
contents=file.readlines()
print(type(contents))
file.close()

print("="*60)

"""수업시간 실습1(read)"""

file = open('file_example.txt','r')
contents = file.read()
file.close()
print(contents)

print("="*60)

file = open('file_example.txt','r')
first_ten_characters= file.read(10)
the_rest= file.read()
file.close()
print('first :',first_ten_characters)
print('the rest :',the_rest)

print("="*60)

"""수업시간 실습2 readlines"""
file=open('planets.txt','r')
planets=file.readlines()
print(planets)
file.close()

print("="*60)

"""strip안하면 \n이 적용되서 출력된다."""

for p in planets :
    print(p)

print("="*60)

"""strip 하면 안 띄어지고 출력되는 것을 확인"""
for p in planets :
    print(p.strip())

print("="*60)

"""reversed, sorted도 적용이 된다"""
for p in reversed(planets) :
    print(p.strip())

print("="*60)

for p in sorted(planets) :
    print(p.strip())

print("="*60)

"""len으로 요소를 세면 strip하면 \n도 세진다. (한 개로 계산) (Week 6 string method)"""
file=open('planets.txt','r')

for line in file :
    print(len(line))

file.close()

print("="*60)

file=open('planets.txt','r')

for line in file :
    print(len(line.strip()))

file.close()

print("="*60)

"""hopedale실습"""

file=open('hopedale.txt','r')
file.readline() #header 첫줄 읽기

data=file.readline().strip() #두번째 줄 data변수에 저장
while data.startswith('#') : #'#'으로 시작하면 출력하지 않고 계속 넘기는 반복문
    data= file.readline().strip()

"""반복문 끝나면 readline했을 때 숫자부터 읽는다"""

for data in file :
    print(data.strip())

file.close()
print("="*60)

"""hopedale data 모두 더하기"""

file=open('hopedale.txt','r')
file.readline() #header 첫줄 읽기

data=file.readline().strip()
while data.startswith('#') :
    data= file.readline().strip()

total=int(data)

for data in file :
    total=total+int(data.strip())

file.close()

print('Total number of pelts :',total)

print("="*60)

"""내가 해본 total 구하기 """
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
    total=total+int(element)

print(total)

print("="*60)

"""인터넷 파일 읽기 (인터넷 파일의 클래스와 그 안의 내용의 클래스도 알아보자)
맥의 경우 sslerror가 나니 certifi 패키지를 설치하고 하자 """

import urllib.request
url="http://robjhyndman.com/tsdldata/ecology1/hopedale.dat"
webpage = urllib.request.urlopen(url)
for line in webpage :
    line=line.strip()
    line=line.decode('utf-8')
    print(line)

print("="*60)

print(type(line))
print(type(webpage))
webpage.close()

print("="*60)

"""로컬파일(내 파일)의 클래스도 살펴보자"""
file=open('hopedale.txt','r')
line=file.readline()
print(type(file))
print(type(line))
file.close()

print("="*60)

"""파일 읽고 쓰기 - number_pairs에 각 줄의 숫자를 더하고 더해서 그 옆에다 작성하기"""
import total
total.sum_number_pairs('number_pairs.txt','out.txt')
out_file=open('out.txt','r')
lines=out_file.readlines()
for line in lines :
    print(line.strip())
print("="*60)
"""skipping the header time_series.py, read_smallest.py 참조 학교방법"""


"""read_smallest"""
import read_smallest
print(read_smallest.smallest_value(open('hebron.txt','r')))

print("="*60)

"""find_largest_1"""

import find_largest_1

file=open('lynx.txt','r')
print(find_largest_1.process_file(file))
file.close()

print("="*60)

"""find_largest_2"""
import find_largest_2

file=open('lynx.txt','r')
print(find_largest_2.process_file(file))
file.close()

print("="*60)


"""직접 실습 (내 방법)"""
file=open('lynx.txt','r')
header=file.readline() #header
lines=file.readlines()#파일의 모든 줄 리스트의 요소에 담기
data=[]#data를 따로 담는 저장공간

for line in lines :
    if not line.startswith('#') : #'#'으로 시작을 안하면 모두 데이터이므로 데이터 변수에 담는다.
        data.append(line.split())

largest=-1 #보초값 지정 데이터는 양수이므로 이 largest는 음수이고 따라서 모든 데이터는 -1보다 크므로 -1을 지정 절대 나올수 없는 값으로 지정
for chunk in data : #리스트안의 리스트를 완전 분해하여 비교해야하므로 이중중첩
    for element in chunk :
        element=int(element[:-1]) #끝에 있는 .을 제거하고 숫자로 타입을 바꿔 크기비교를 할 수있도록 하는 작업
        if element>largest : #모든 값을 체크해서 element가 큰 것을 largest변수에 저장
            largest=element
file.close()
print(largest)

print("="*60)

"""Multiline records"""
import molecules
file=open('multimol.pdb','r')
print(molecules.read_all_molecules(file))
file.close()

print("="*60)

import molecules2
file=open('multimlol.pdb','r')
print(molecules2.read_all_molecules(file))
file.close()

print("="*60)

"""내방법"""

file=open('multimol.pdb','r')

count=0
lines = file.readlines()
for line in lines :
    line.strip()
    if line.startswith("COMPND") :
        count=count+1

#compound의 개수를 구하기

molecule=[]
result=[]
while count>0 :
    for line in lines :
        if line.startswith("COMPND") : #분자 이름 molecule에 담고
            compound, name = line.split()
            molecule.append(name)
        elif line.startswith("ATOM") : #Atom의 결과값을 담는다
            key, num, atom_type, x, y, z = line.split()
            molecule.append([atom_type, x, y, z])
        else :
            result.append(molecule) #END가 나오면 molecule을  result에담고
            molecule.clear() # molecule 초기화
            count=count-1 #하나 다 센 것이므로 count개수를 줄인다.

print(result)



file.close()

print("="*60)