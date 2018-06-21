#for 문 사용 리스트 요소 만들기(검색 실험 리스트 생성 코드)
elements_number=int(input("요소의 개수를 정하세요 : "))
list_default=[]
from random import randint
for i in range(elements_number) :
    list_element = randint(1, elements_number*10)
    if list_element in list_default : continue
    list_default.append(list_element)
list1=list_default[:]
list1.sort()
value_want=int(input("찾을 값은 ?"))


#linear search while문

def linear_search_while(L,value_want) :
    index = 0 #변수 초기화
    while index != len(L) and value_want != L[index]: #찾는 값과 리스트[위치] 값이 같거나 index값이 라스트 요소의 개수만큼 되면 반복문을 빠져나온다.
        index = index + 1#반복을 하는동안 index 의 값을 1씩 증가시켜 하나하나 찾는다.
    if index == len(L): #반복을 다해서 결국 index값이 리스트 요소의 개수가 되면(마지막까지 찾았다는 뜻 == 찾는 값이 리스트에 없다)
                        #찾는 값이 리스트에 없으면 실행
        value_want_index = -1 #찾는값이 리스트에 없으면 -1을 리턴
    else:
        value_want_index = index #찾는 값이 있어 반복문을 빠져나왔을 때 index값은 찾는 값이 위치해있는 리스트의 index값과 같기 때문에
                                 # 그때 index 를 리턴한다.
    return value_want_index

#linear search for문

def linear_search_for(L,value_want) :
    for a in range(len(L)): #0,1,2,3,4... 함수 길이 -1까지 반복
        if L[a] == value_want: # 리스트[위치]에서 찾는 값이 같으면
            return a #return 을 만나면 함수를 빠져나기 성질을 이용해 따로 break를 넣지않고도 조건을 만족 했을 때 for문의 반복을 멈출 수 있다

    return -1 #for문이 끝까지돌고 끝나면 찾는 값이 없는 것으로 판단 -1을 리턴(함수 빠져나간다.)


#sentinel_linear_search

#찾는 값을 sentinel로 지정 데이터 끝에 위치시켜 데이터의 종료를 알린다.
def sentinel_linear_search(L,value_want) :
    L.append(value_want) #찾는 값을 sentinel로 지정할 것이므로 append를 써 리스트의 맨 마지막에 추가한다.
    trial_time = 0
    while L[trial_time] != value_want: #linear_search와 다른 점은 while의 조건이 하나이므로 한번의 연산만 거치면 된다는 것이다.
        trial_time = trial_time + 1
    L.pop()
    if trial_time == len(L):
        value_want_index = -1
    else:
        value_want_index = trial_time
    return value_want_index
"""pop으로 꺼내는 이유 : 처음에 찾을 값을 리스트의 마지막에 위치한 것을 알고있는 상태이고 그러면 while문으로 찾는 행위를 반복하다가 보면 마지막에 무조건 찾게 되어 while문을 종료한다.

그 러면 우리가 지정한 i(1씩 증가하도록 만든 변수)는 리스트의 마지막 index번호가 된 상태이다.

안꺼내면  if 에서 index번호가 ==len(list)라고 해 못찾으면 -1로 반환하려고하는데 뒤에 하나를 추가하고 안 꺼내면 

index번호는 len(list)와 무조건 같을 수가 없으므로 (len(list)가 무조건 index보다 1 이 크다(파이썬은 index가 0부터 시작하므로))

결국 출력하는 index번호는 -1은 절대 안나오고 끝난 리스트의 마지막 index번호를 리턴한다.

그런데 이 index번호는 기존의 리스트에서 벗어난 index이므로 우리가 원하는 값이 나오지 않게 되는 것이다."""

"""
   pop으로 꺼낸 후 판단하는 것이니 len(L)값은 기존의 리스트 요소의 개수가 될 것이다.

   따라서 못찾으면 trial_time과 len(L)값은 같아질 수 밖에 없다
   
   못찾으면 -1 리턴
   
   찾으면 반복이 종료되고 그 때 trial_time값이 찾는 값의 index가 될 것이다.
"""


#list.index
#요소가 있는지 리스트 매서드 index로 판단 그리고 있으면 index 리턴 없으면 오류가 나므로 오류를 잡아주고 해당 오류가 났을때 index값을 -1로 하면 된다.
def list_index(L,value_want) :
    try:
        value_want_index = L.index(value_want)
    except ValueError:
        value_want_index = -1
    return value_want_index


#Binary search
#정렬된 리스트 여야 한다.(정렬된 시간은 빼고 계산해야한다.)(정렬되있음을 가정하고 코드를 짜보자)
def binary_search(L,value_want) :
    first_number = 0  # 첫번 째 인덱스 값
    last_number = len(L) - 1  # 마지막 인덱스 값
    while first_number <= last_number :
        middle_number = (first_number + last_number) // 2 # int가 나와야하므로 integer divide로 한다. 계속 업데이트 되어야하므로 while 블록안에 넣는다
        if value_want > L[middle_number]: #반보다 클 때 반 값 뒤에 있는 부분 부터 마지막 부분 만 남긴다 (반 값은 이미 비교했으므로 할 필요 없다.)
            first_number = middle_number+1
        elif value_want < L[middle_number] : #반 보 다 작을 때 처음 부분 부터 반 값 앞에 있는 부분만 남긴다. (반 값은 이미 비교했으므로 할 필요 없다.)
            last_number = middle_number-1
        else : #반복문 중간에 반 값이 찾던 값과 같다면 return으로 함수를 빠져나가므로 while문도 빠져나가게 된다 def 안이 아니면 따로 break를 걸거나 while문 조건에 추가해야한다.
            return middle_number
    return -1 #반으로 계속 자르다가 찾는 값이 없다면 계산상 무조건 적으로 first 는 last와 같거나 크게 된다. 그럴 때 반복문을 빠져나오고 함수가 끝나는 return을 만나 -1을 출력한다.
    #

#Binary_search_in the book
def binary_search_book(L,value_want) :
    first_number= 0
    last_number =len(L) -1
    while first_number != last_number+1 :
        middle_number=(first_number+last_number)//2
        if value_want > L[middle_number] :
            first_number=middle_number+1
        else :
            last_number=middle_number-1
    if 0<=first_number<len(L) and value_want==L[first_number] :
        return first_number
    else :
        return -1

#파이썬 라이브러리 bisect이용 중복된 값 없으므로 bisect(list,value_want,beg,end) 이용
from bisect import bisect

#시간 비교
import time

def convert_to_mS(time):
    return time*pow(10,3)

t1_linear_while=time.perf_counter()
linear_search_while(list_default,value_want)
t2_linear_while=time.perf_counter()

time_linear_while=(t2_linear_while-t1_linear_while)

t1_linear_for=time.perf_counter()
linear_search_for(list_default,value_want)
t2_linear_for=time.perf_counter()

time_linear_for=(t2_linear_for-t1_linear_for)

t1_sentinel=time.perf_counter()
sentinel_linear_search(list_default,value_want)
t2_sentinel=time.perf_counter()

time_sentinel=(t2_sentinel-t1_sentinel)

t1_list_index=time.perf_counter()
list_index(list_default,value_want)
t2_list_index=time.perf_counter()

time_list_index=(t2_list_index-t1_list_index)

t1_binary_search=time.perf_counter()
binary_search(list1,value_want)
t2_binary_search=time.perf_counter()

time_binary=(t2_binary_search-t1_binary_search)

t1_binary_book=time.perf_counter()
binary_search_book(list1,value_want)
t2_binary_book=time.perf_counter()

time_binary_book=(t2_binary_book-t1_binary_book)

t1_bisect=time.perf_counter()
bisect(list_default,value_want)
t2_bisect=time.perf_counter()

time_bisect=(t2_bisect-t1_bisect)

#각 알고리즘 시간 정리
time_storage=[time_linear_while,time_linear_for,time_sentinel,time_list_index,time_binary,time_binary_book,time_bisect]

time_storage_mS=[]
for a in time_storage :
    time_storage_mS.append(convert_to_mS(a))

time_dict=dict(zip(time_storage_mS,["time_linear_while","time_linear_for","time_sentinel","time_list_index","time_binary","time_binary_book","time_bisect"]))
time_dict_key=list(time_dict.keys())
time_dict_key.sort()

#출력 값
for i in range(len(time_dict_key)) :
    print("{rank}등은 {time_name}, 걸린 시간은 {time}mS입니다.".format(rank=i+1,time_name=time_dict[time_dict_key[i]],time=round(time_dict_key[i],2)))


