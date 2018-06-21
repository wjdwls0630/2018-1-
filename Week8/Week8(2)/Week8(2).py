"""set 책 예시"""

observations_file = open('observations.txt','r') #파일 열기
birds_observed = set() #빈 set 생성
for line in observations_file: #파일의 모든줄을 반복
    bird = line.strip() #공백제거
    birds_observed.add(bird) #하나의 항목을 빈 set에 추가 하기

print(birds_observed) #중복이 제거된 상태로 순서는 없이 set이 생성된것을 확인 가능

observations_file.close()
print("="*60)

for species in birds_observed:
    print(species)

print("="*60)

"""dictionary 책 예시"""
observations_file = open('observations.txt','r') #파일 열고
bird_to_observations = {} #빈 딕셔너리 생성

for line in observations_file: #파일의 모든 줄 읽고
    bird = line.strip() #줄의 공백 제거
    if bird in bird_to_observations: #만약 딕셔너리에 bird(key)가 있다면
        bird_to_observations[bird] = bird_to_observations[bird] + 1 #해당 bird(key)의 value값을 1 증가시킨다
    else: #없다면
        bird_to_observations[bird] = 1 #bird :1 항목을 추가시킨다

observations_file.close()

for bird, observations in bird_to_observations.items(): #dict_items객체를 확인해보면  [(key,value), () ,....] 형식
    print(bird, observations)


print("="*60)


"""dictionary 책 예시 2"""

observations_file = open('observations.txt','r')
bird_to_observations = {}

for line in observations_file:
    bird = line.strip()
    bird_to_observations[bird] = bird_to_observations.get(bird, 0) + 1
    #bird가 있으면 기존 value값에 1을 더하는 것이고 없으면 get이 0을 리턴하므로 새로운 bird:1이 추가된다.

observations_file.close()

for bird, observations in bird_to_observations.items():
    print(bird, observations)

print("="*60)

"""dictionary 예시 2 다른 방법(collection 라이브러리에서 defaultdict함수 이용"""
from collections import defaultdict
observations_file = open('observations.txt','r')
bird_to_observations = defaultdict(int)
#bird_to_observations의 디폴트 값은 int라는 것을 설정 그러면 해당 key값이 없으면 자동으로 int초기값인 0이 배정이 된다.

for line in observations_file:
    bird = line.strip()
    bird_to_observations[bird] = bird_to_observations[bird]+1
    #bird가 있으면 기존 value값에 1을 더하는 것이고 없으면 get이 0을 리턴하므로 새로운 bird:1이 추가된다.

observations_file.close()

for bird, observations in bird_to_observations.items():
    print(bird, observations)

#결과가 같은 것을 알 수 있다.
print("="*60)