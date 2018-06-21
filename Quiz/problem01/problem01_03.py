def get_score(grade): #1개의 grade값을 평점으로 변환해주는 함수
	if grade =="A":
		score=4.0
	elif grade == "B":
		score=3.0
	elif grade == "C":
		score=2.0
	elif grade == "D":
		score=1.0
	else :
		score=0.0
	return score

English_grade=input("What\'s the grade for English? ")
Physics_grade=input("What\'s the grade for Physics? ")
Programming_grade=input("What\'s the grade for Programming? ")


GPA=(get_score(English_grade)+get_score(Programming_grade)+get_score(Physics_grade))/3
print("GPA is",round(GPA,2))
#round 함수는 반올림? 해주는 함수 인데 입력한 값의 가장 가까운 정수형의 숫자를 return해준다.
#round(x,y)가 기본 입력형 -> y를 안 쓰면 정수형의 숫자를 return하고 y에 값을 넣으면 x를 소수점 y번째 자리까지 반올림해서 return한다.