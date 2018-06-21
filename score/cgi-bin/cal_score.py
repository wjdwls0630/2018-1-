import os, Exam
os.chdir('cgi-bin')
file=open('score2.txt','r')
score_table=[]
for line in file :
    information=line.split()
    score_table.append(information)


#각 항목 당 테이블에 저장
Student_table=[]
Quiz_table=[]
Midterm1_table=[]
Midterm2_table=[]
All_Total_table=[]
for i in range(len(score_table)) :
    student_id = score_table[i][0]
    quiz_1_score = float(score_table[i][1])
    quiz_2_score = float(score_table[i][2])
    quiz_3_score = float(score_table[i][3])
    quiz_4_score = float(score_table[i][4])
    quiz_5_score = float(score_table[i][5])
    quiz_6_score = float(score_table[i][6])
    quiz_7_score = float(score_table[i][7])
    mid1_1_score = float(score_table[i][8])
    mid1_2_score = float(score_table[i][9])
    mid1_3_score = float(score_table[i][10])
    mid1_4_score = float(score_table[i][11])
    mid1_5_score = float(score_table[i][12])
    mid1_total_score = float(score_table[i][13])
    mid2_1_score = float(score_table[i][14])
    mid2_2_score = float(score_table[i][15])
    mid2_3_score = float(score_table[i][16])
    mid2_4_score = float(score_table[i][17])
    mid2_5_score = float(score_table[i][18])
    mid2_total_score = float(score_table[i][19])
    a=Exam.Quiz(student_id,quiz_1_score,quiz_2_score,quiz_3_score,quiz_4_score,quiz_5_score,quiz_6_score,quiz_7_score)
    b=Exam.Midterm1(student_id,mid1_1_score,mid1_2_score,mid1_3_score,mid1_4_score,mid1_5_score,mid1_total_score)
    c=Exam.Midterm2(student_id,mid2_1_score,mid2_2_score,mid2_3_score,mid2_4_score,mid2_5_score,mid2_total_score)
    d=Exam.Total(student_id,quiz_1_score+quiz_2_score+quiz_3_score+quiz_4_score+quiz_5_score+quiz_6_score+quiz_7_score,mid1_total_score,mid2_total_score)
    e=Exam.Student(student_id)
    Quiz_table.append(a)
    Midterm1_table.append(b)
    Midterm2_table.append(c)
    All_Total_table.append(d)
    Student_table.append(e)

#높은 성적 순으로 정렬
from operator import attrgetter

Quiz_table.sort(key=attrgetter('total'),reverse=True)

Midterm1_table.sort(key=attrgetter('total'),reverse=True)

Midterm2_table.sort(key=attrgetter('total'),reverse=True)

All_Total_table.sort(key=attrgetter('all_total'),reverse=True)



















