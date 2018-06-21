from random import randint
num_list=[]
#리스트 길이 수정 가능 , 숫자 범위 수정 가능
while len(num_list) < 10 :
    a = randint(1, 20)
    if a in num_list :
        continue
    else:
        num_list.append(a)

user_num=int(input("추가할 숫자를 입력하세요 : "))

# 주어진 문제 에서 절대값 차의 합을 구하는 함수
def calculate(list) :
    total=0
    for i in range(len(list)-1) :
        result = abs(list[i] - list[i + 1])
        total += result
    return total

#제대로 동작하는지 확인
for i in range(len(num_list)+1) :
    num_list.insert(i,user_num)
    print(num_list,calculate(num_list))
    num_list.remove(user_num)

#solution 리스트를 따로만들어 인덱스가 같으므로 해당 위치에 인덱스를 사용한다.
#max도 기본적으로 찾을 때 가장 먼저 나온(index값이 가장 작은) max값을 찾으므로 문제 조건과 동일하다
total_list=[]
for i in range(len(num_list)) :
    num_list.insert(i,user_num)
    total_list.append(calculate(num_list))
    num_list.remove(user_num)

total_max_index=total_list.index(max(total_list))
num_list.insert(total_max_index,user_num)
print("합이 최대가 되는 위치 : {}\n합이 최대가 되는 리스트 : {}\n합 : {}".format(total_max_index,num_list,total_list[total_max_index]))

# do not modify num_list
num_list = [1, 9, 3, 4, 2, 5, 7, 6, 8]
a = int(input())

num = num_list[:]
for i in range(len(num)):
    value[i] = value[i] - a


