#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
print ("Content-Type: text/plain; charset=utf-8\n\n")
import cgi, View
from cal_score import Student_table
form=cgi.FieldStorage()
student_id = form['user_id'].value
option = form['option'].value
def view(student_id) :
    for i in Student_table:
        if i.id == student_id:
            if option == 'Quiz':
                result=View.view_quiz(student_id)
            elif option == 'Mid1':
                result=View.view_mid1(student_id)
            elif option == 'Mid2':
                result=View.view_mid2(student_id)
            elif option == 'Total':
                View.view_total(student_id)
            elif option == 'All':
                result=View.view_quiz(student_id)+View.view_mid1(student_id)+View.view_mid2(student_id)+View.view_total(student_id)
            return result

    return "학번을 잘 못 입력하셨습니다. 다시 index 페이지로 돌아가세요."



print(view(student_id))



















