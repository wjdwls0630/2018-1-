class Student() :
    def __init__(self,id=""):
        self.id=id
    def __repr__(self):
        return repr([self.id])

class Quiz() :
    def __init__(self,id="",q1=0.0,q2=0.0,q3=0.0,q4=0.0,q5=0.0,q6=0.0,q7=0.0,q8=30.0,q9=30.0,q10=30.0):
        self.id=id
        self.q1=(q1)
        self.q2=(q2)
        self.q3=(q3)
        self.q4=(q4)
        self.q5 = (q5)
        self.q6 = (q6)
        self.q7 = (q7)
        self.q8 = (q8)
        self.q9 = (q9)
        self.q10 = (q10)
        self.total=(self.q1+self.q2+self.q3+self.q4+self.q5+self.q6+self.q7+self.q8+self.q9+self.q10)

    def getAverage(self):
        result=self.total/10
        return result
    def __repr__(self):
        return repr([self.id,self.q1,self.q2,self.q3,self.q4,self.q5,self.q6,self.q7,self.total])

    def __str__(self):
        a="학번 : {}\n".format(self.id)
        b = "quiz1 점수 : {}\n".format(self.q1)
        c = "quiz2 점수 : {}\n".format(self.q2)
        d = "quiz3 점수 : {}\n".format(self.q3)
        e = "quiz4 점수 : {}\n".format(self.q4)
        f = "quiz5 점수 : {}\n".format(self.q5)
        g = "quiz6 점수 : {}\n".format(self.q6)
        h = "quiz7 점수 : {}\n".format(self.q7)
        i = "quiz8 점수 : {}\n".format(self.q8)
        j = "quiz9 점수 : {}\n".format(self.q9)
        k = "quiz10 점수 : {}\n".format(self.q10)
        m = "quiz 총합 점수 : {}\n".format(self.total)
        n = "quiz 평균 점수 (한 문제 당) : {}\n\n".format(Quiz.getAverage(self))
        return a+b+c+d+e+f+g+h+i+j+k+m+n

class Midterm1() :
    def __init__(self,id="",q1=0.0,q2=0.0,q3=0.0,q4=0.0,q5=0.0,total=0.0):
        self.id=id
        self.q1=(q1)
        self.q2=(q2)
        self.q3=(q3)
        self.q4=(q4)
        self.q5 = (q5)
        self.total=(total)

    def getAverage(self):
        result=self.total/5
        return result

    def __str__(self):
        a="학번 : {}\n".format(self.id)
        b = "mid1_q1 점수 : {}\n".format(self.q1)
        c = "mid1_q2 점수 : {}\n".format(self.q2)
        d = "mid1_q3 점수 : {}\n".format(self.q3)
        e = "mid1_q4 점수 : {}\n".format(self.q4)
        f = "mid1_q5 점수 : {}\n".format(self.q5)
        g = "mid1 총합 점수 : {}\n".format(self.total)
        h = "mid1 평균 점수(한 문제 당) : {}\n\n".format(Midterm1.getAverage(self))
        return a+b+c+d+e+f+g+h

    def __repr__(self):
        return repr([self.id,self.q1,self.q2,self.q3,self.q4,self.q5,self.total])

class Midterm2(Midterm1) :

    def __str__(self):
        a = "학번 : {}\n".format(self.id)
        b = "mid2_q1 점수 : {}\n".format(self.q1)
        c = "mid2_q2 점수 : {}\n".format(self.q2)
        d = "mid2_q3 점수 : {}\n".format(self.q3)
        e = "mid2_q4 점수 : {}\n".format(self.q4)
        f = "mid2_q5 점수 : {}\n".format(self.q5)
        g = "mid2 총합 점수 : {}\n".format(self.total)
        h = "mid2 평균 점수(한 문제 당) : {}\n\n".format(Midterm1.getAverage(self))
        return a+b+c+d+e+f+g+h

class Total() :
    def __init__(self,id="",quiz_total=0.0,mid1_total=0.0,mid2_total=0.0):
        self.id=id
        self.quiz_total=(quiz_total)
        self.mid1_total=(mid1_total)
        self.mid2_total=(mid2_total)
        self.all_total=(self.quiz_total*0.1+mid1_total*0.2+mid2_total*0.2)
    def __str__(self):
        a="학번 : {}\n".format(self.id)
        b="총점 계산(퀴즈 30%, 1차시험 20%, 2차시험 20%, 출석 10%) : {}점입니다.\n\n".format(self.all_total)
        return a+b
    def __repr__(self):
        return repr([self.id,self.mid1_total,self.mid2_total,self.all_total])