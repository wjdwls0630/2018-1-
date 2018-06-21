#Algorithms

'''
리스트 요소는 random module로 생성하겠다.
리스트 요소는 무작위로 만들어지고 마지막 번호로 계속 리스트에 추가된다.
이후 set화 시켜 중복요소를 제거하고 다시 리스트화 시킨다.(중복제거는 되었지만 정렬이 되지 않은 상태)
set하고 돌리면 생각보다 정렬이 잘 된다. 무작위로 뽑은 숫자가 중복되면 앞에 있는 숫자부터 지워져서 확률적으로 크기 순서대로 배열이 될 듯 하다.
중복된 요소를 제거하되 앞에 있는 숫자가 남게 해야겠다.
나머지 리스트를 분석할때 똑같은 리스트를 사용할 수 있도록 default리스트를 하나 만들어둔다.
'''

'''
#for 문 사용 리스트 요소 만들기
elements_number=int(input("요소의 개수를 정하세요 : "))
list_default=[]
from random import randint
for i in range(elements_number) :
    list_element = randint(1, elements_number*10)
    if list_element in list_default : continue #만든 난수가 이미 있으면 append하지않고 for문의 처음으로 돌아가 다시 난수를 생성한다.
    list_default.append(list_element)
'''


'''
이 방법은 입력값으로 입력한 처음 요소의 개수를 무조건 채울 수가 없다 요소의 개수가 적으면 완성될 확률이 높아지는데 요소의 숫자가 많아질 수록 손실이 많다.
pow의 크기를 더 키우면 되지만 컴퓨터의 프로세스가 너무 많이 걸리고 비효율적이다 조금 더 괜찮은 방법이 있을 것 같다.
그냥 크기는 10을 곱하고 해야겠다.
'''

'''
#while 문으로 만들어보자.
from random import randint
elements_number=int(input("요소의 개수를 정하세요 : "))
list_default=[]
while len(list_default) != elements_number : #같아지면 while 문 중단
    #생각해보니 pow나 범위를 넓히는 것은 무조건 들어가야 할 것 같다. 그냥 randint (1,100)하면 100부터 1까지 다 들어 가있을 테니
    #원하는 리스트의 모습이 아니다 .  대신 100정도 곱하고 원하는 요소 개수를 채워야할 듯 하다 . 100부터 정말로 무작위 일 것 같다
    #10도 가능하지만 완전 무작위 느낌이 아니라서 욕심내서 100을 해야겠다.
    #100으로 하니 너무 큰 수일때는 실행시간이 너무 오래걸린다 10으로 해야겠다.
    #다른 범위를 계속 넣어주면 더 좋아질까 싶어 일단 보류
    #10으로 하고 조금 범위를 십만까지만 해야겠다 백만 해보니까 찾는데 너무 오래걸린다.
    #요소의 개수 범위마다 난수 범위를 조절해야겠다.
    #이러면 조건 도 많아지고 프로세스도 길어지니까 의미가 없다 처음 코드를 사용하고 개수를 꽉 채울라는 시도는 포기해야겠다.
    if 0<=elements_number<10 : #한자리
        list_element=randint(1,elements_number*pow(10,4))
    elif elements_number<100 : #두자리
        list_element=randint(1,elements_number*pow(10,3))
    elif elements_number<1000 :
        list_element=randint(1,elements_number*pow(10,2))
    elif elements_number<10000 :
        list_element=randint(1,elements_number*10)
    elif elements_number<100000 :
        list_element = randint(1,elements_number*9)
    else :
        list_element= randint(1,elements_number)
        if len(list_default)==100000 : break
    if list_element not in list_default :
        list_default.append(list_element)

print(len(list_default))
'''


#searching algorithms

#Find,remove ,find Algorithms
def find_two_smallest_FRF(L) :
    min1 = min(L)
    min1_index = L.index(min1)
    L.remove(min1)
    min2 = min(L)
    L.insert(min1_index, min1)
    min2_index = L.index(min2)
    result=(min1_index, min2_index)
    return result


#sort,identify minimums, get indices
def find_two_smallest_SIG(L) :
    list2 = L[:]
    list2.sort()
    min1 = list2[0]
    min2 = list2[1]
    min1_index = L.index(min1)
    min2_index = L.index(min2)
    result = (min1_index, min2_index)
    return result

#Walk through the list
def find_two_smallest_WTL(L) :
    if L[0] < L[1]:
        min1_index = 0
        min2_index = 1
    else:
        min1_index = 1
        min2_index = 0
    for i in range(len(L)):
        if L[i] < L[min1_index]:
            min2_index = min1_index
            min1_index = i
        elif L[i] < L[min2_index]:
            min2_index = i
        else:
            pass
    result=(min1_index, min2_index)
    return result

#for 문 사용 리스트 요소 만들기(검색 실험 리스트 생성 코드)
elements_number=int(input("요소의 개수를 정하세요 : "))
list_default=[]
from random import randint
for i in range(elements_number) :
    list_element = randint(1, elements_number*10)
    if list_element in list_default : continue
    list_default.append(list_element)

def convert_to_mS(time):
    return time*pow(10,3)

#알고리즘 시간 비교
import time
t1_FRF=time.perf_counter()
find_two_smallest_FRF(list_default)
t2_FRF=time.perf_counter()

FRF_time=t2_FRF-t1_FRF

t1_SIG=time.perf_counter()
find_two_smallest_SIG(list_default)
t2_SIG=time.perf_counter()

SIG_time=t2_SIG-t1_SIG

t1_WTL=time.perf_counter()
find_two_smallest_WTL(list_default)
t2_WTL=time.perf_counter()

WTL_time=t2_WTL-t1_WTL


#각 알고리즘 시간 정리
time_storage=[FRF_time,SIG_time,WTL_time]
time_storage_mS=[]
for a in time_storage :
    time_storage_mS.append(convert_to_mS(a))

time_dict=dict(zip(time_storage_mS,["FRF_time","SIG_time","WTL_time"]))
time_dict_key=list(time_dict.keys())
time_dict_key.sort()

for i in range(len(time_dict_key)) :
    print("{rank}등은 {time_name}, 걸린 시간은 {time}mS입니다.".format(rank=i+1,time_name=time_dict[time_dict_key[i]],time=round(time_dict_key[i],2)))
