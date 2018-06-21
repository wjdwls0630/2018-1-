#무작위 리스트 생성
user_range=int(input("자료의 크기는 ? : "))
list_default=[]
from random import randint

while len(list_default) != user_range :
    list_element=randint(1,user_range)
    if list_element in list_default : continue
    list_default.append(list_element)

"""요소의 개수는 자료의 크기가 딱 맞게 끔 하기 위해 while문으로 작성 했고 중복 없이 범위 안의 숫자들을 무작위 배치되게 하는 리스트를 만들었다."""
#두 요소의 위치를 서로 바꾸는 함수
def change (L, i ,j) :
    L[i], L[j] = L[j], L[i]

#bubble sort

def bubble_sort (L) :
    if len(L)<1 :
        return L
    for size in reversed(range(len(L))): #1~n까지 len = n / n-1,n-2,....0 순으로 들어간다.
        for i in range(size): #n-1부터 0~n-2까지 들어가므로 index가 오버되지 않는다.
            if L[i] > L[i + 1]:
                change(L,i,i+1)
    return L
"""
큰 숫자를 뒤로 계속 보내므로 첫 번째 실행했을 때 맨 뒤로 보내지는 것은 그 리스트 안의 가장 큰 수 이다.
그렇게 계속 차곡차곡 뒤에서부터 쌓는 것이므로 첫 번째 수행 부터 마지막 index (n-1) 는 정렬을 안해도 되고 두 번째하면 n-2 도 비교를 안해도 되므로 
횟수는 딱 for 문이 리스트 요소 개수 n 만큼 행하면 된다.
연산이 다 진행되면 그냥 연산하지 않고 넘기기 때문에 신경 쓰지 않아도 된다.
"""

#selection sort
def selection_sort(L) :
    if len(L)<1 :
        return L
    min1_index = 0
    for index in range(len(L)): #1~n까지 len = n / 0,1,2,3....n-1 순으로 들어간다.
        for i in range(index + 1, len(L)): #0부터 1~n-1까지 들어간다 첫번째 부터 마지막까지 훑고 1부터 는 2~n-1까지 두번째 부터 마지막까지 훑는것 ...
            if L[min1_index] > L[i]:
                min1_index = i
        change(L, index, min1_index)
    return L


"""
안에 있는 for문에서 minimum값을 범위 안에 모든 요소를 체크하고 만약 체크하다 minimum값을 만나면 해당 index를 업데이트 한다.
안에있는 for문의 첫번째 루프에서 첫번째 요소와 나머지 두번째 부터 마지막까지 의 요소를 비교하므로 첫번째 루프에서 생성된 minimum 은 무조건 리스트의 최소값이므로 index=0번에 배정하고 
바깥 for문으로 넘어가 두번째 바깥 for문 루프를 실행한다.
안에 있는 for문 부터는 두번째로 작은 요소를 비교해서 업데이트 하고 index 1번에 배정하고 다시 바깥 for 문으로 넘어가 세번째 바깥 for문 루프를 실행한다.
이런식으로 마지막까지 비교해서 작은값부터 앞 쪽으로 배정해서 정렬한다.
"""

#insertion sort
def insertion_sort(L) :
    if len(L)<1 :
        return L
    for size in range(1, len(L)): #1부터 마지막 요소 까지 실행 비교할 자료의 크기를 정하는 for문
        element = L[size]  # 자료의 크기중 마지막 요소(값)를 저장 -> 이 것을 비교할 것
        index = size  # 마지막 요소의 index번호 설정 - index변수 초기화

        while index > 0 and L[index - 1] > element:  # 앞에 있는 요소보다 자신이 크면 비교 중단 후 그 자리에 삽입 자신이 작으면 한 칸 앞으로 이동
            L[index] = L[index - 1]  # 한 칸 씩 뒤로 밀리는 과정 그 앞 위치에 있는 값을 한 칸 뒤 위치에 배치
            index = index - 1  # index 위치를 하나 앞으로 간다.
        L[index] = element  # while문이 중단되고 실행되는 코드 - 맨 앞으로 갔거나(index=0인 상태) 그 index 위치에서 앞의 요소랑 비교했을 때 크므로 while문 빠져나오고
        #그 때 위치가 자신의 위치이므로 반복문이 끝난 index위치에 element 삽입
    return L


#merge sort
def merge_sort(L):
    #divide
    if len(L) <= 1:#요소가 0개, 1개면 정렬 할 필요없이 입력값을 돌려주면 된다
        return L
    middle_number = len(L) // 2 #가운데 index
    left_L = L[:middle_number]
    right_L = L[middle_number:]
    left_L = merge_sort(left_L)
    right_L = merge_sort(right_L)
    """재귀함수로 다시 자기 자신을 호출해 요소가 1개가 될 때까지 처리가 되지 않은 상태로 남겨지고 merge로 left right 변수에 정렬된 리스트를 다시 할당한다 """
    #merge
    return merge(left_L, right_L)

def merge(left_L, right_L):
    list_sort = [] #정렬된 리스트를 받을 새로운 리스트를 생성 - 따라서 메모리 사용량을 두배로 사용 할 것같다.
    while len(left_L) > 0 or len(right_L) > 0:
        if len(left_L) > 0 and len(right_L) > 0:
            if left_L[0] <= right_L[0]:
                list_sort.append(left_L[0])
                left_L = left_L[1:] #빼낸 요소는 기존 리스트에서 제거하는 과정
            else:
                list_sort.append(right_L[0])
                right_L = right_L[1:]
        elif len(left_L) > 0:
            list_sort.append(left_L[0])
            left_L = left_L[1:]
        elif len(right_L) > 0:
            list_sort.append(right_L[0])
            right_L = right_L[1:]
    return list_sort


import time

def convert_to_mS(time):
    return time*pow(10,3)

t1_bubble=time.perf_counter()
bubble_sort(list_default)
t2_bubble=time.perf_counter()

time_bubble=(t2_bubble-t1_bubble)

t1_selection=time.perf_counter()
selection_sort(list_default)
t2_selection=time.perf_counter()

time_selection=(t2_selection-t1_selection)

t1_insertion=time.perf_counter()
insertion_sort(list_default)
t2_insertion=time.perf_counter()

time_insertion=(t2_insertion-t1_insertion)

t1_merge=time.perf_counter()
merge_sort(list_default)
t2_merge=time.perf_counter()

time_merge=(t2_merge-t1_merge)

t1_sort=time.perf_counter()
list_default.sort()
t2_sort=time.perf_counter()

time_sort=(t2_sort-t1_sort)
#각 정렬 시간 정리
time_storage=[time_bubble,time_selection,time_insertion,time_merge,time_sort]

time_storage_mS=[]
for a in time_storage :
    time_storage_mS.append(convert_to_mS(a))

time_dict=dict(zip(time_storage_mS,["time_bubble","time_selection","time_insertion","time_merge","time_sort"]))
time_dict_key=list(time_dict.keys())
time_dict_key.sort()

#출력 값
for i in range(len(time_dict_key)) :
    print("{rank}등은 {time_name}, 걸린 시간은 {time}mS입니다.".format(rank=i+1,time_name=time_dict[time_dict_key[i]],time=round(time_dict_key[i],2)))

