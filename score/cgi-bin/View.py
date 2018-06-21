from cal_score import Quiz_table, Midterm1_table, Midterm2_table, All_Total_table
#자신 점수 보기
user_id=""
def view_quiz(user_id):
    result="="*60+"\n"
    quiz_rank = 1
    quiz_rank_count = 0
    quiz_rank_score = 300
    for i in Quiz_table:
        if quiz_rank_score == i.total:
            quiz_rank_count += 1
        else:
            quiz_rank_score = i.total
            if quiz_rank_count == 0:
                quiz_rank_count = 1
            quiz_rank += quiz_rank_count
            quiz_rank_count = 0
        if i.id == user_id:
            result+=str(i)
            result+="퀴즈에서 {}등입니다!\n\n".format(quiz_rank)
            result+="상위 {}%입니다!\n\n".format(round((quiz_rank / len(Quiz_table)) * 100, 3))
            break

    # 전체 학생 퀴즈 평균
    quiz_total = 0
    for i in Quiz_table:
        quiz_total += i.total
    quiz_total_average = quiz_total / len(Quiz_table)
    result+="전체 학생 퀴즈 평균은 {}점 입니다.\n".format(quiz_total_average)
    result+="="*60+"\n"
    return result


def view_mid1(user_id) :
    result="="*60+"\n"
    mid1_rank = 1
    mid1_rank_count = 0
    mid1_rank_score = 100
    for i in Midterm1_table:
        if mid1_rank_score == i.total:
            mid1_rank_count += 1
        else:
            mid1_rank_score = i.total
            if mid1_rank_count == 0:
                mid1_rank_count = 1
            mid1_rank += mid1_rank_count
            mid1_rank_count = 0
        if i.id == user_id:
            result+=str(i)
            result+="1차 시험에서 {}등입니다!\n\n".format(mid1_rank)
            result+="상위 {}%입니다!\n\n".format(round((mid1_rank / len(Midterm1_table)) * 100, 3))
            break

    # 전체 학생 midterm1 평균
    mid1_total = 0
    for i in Midterm1_table:
        mid1_total += i.total
    mid1_total_average = mid1_total / len(Midterm1_table)
    result+="전체 학생 1차 시험 평균은 {}점 입니다.\n".format(mid1_total_average)
    result+="=" * 60+"\n"
    return result

def view_mid2(user_id) :
    result="=" * 60+"\n"
    mid2_rank = 1
    mid2_rank_count = 0
    mid2_rank_score = 100
    for i in Midterm2_table:
        if mid2_rank_score == i.total:
            mid2_rank_count += 1
        else:
            mid2_rank_score = i.total
            if mid2_rank_count == 0:
                mid2_rank_count = 1
            mid2_rank += mid2_rank_count
            mid2_rank_count = 0
        if i.id == user_id:
            result +=str(i)
            result+="2차 시험에서 {}등입니다!\n\n".format(mid2_rank)
            result+="상위 {}%입니다!\n\n".format(round((mid2_rank / len(Midterm2_table)) * 100, 3))
            break

    # 전체 학생 midterm2평균
    mid2_total = 0
    for i in Midterm2_table:
        mid2_total += i.total
    mid2_total_average = mid2_total / len(Midterm2_table)
    result+="전체 학생 2차 시험 평균은 {}점 입니다.\n".format(mid2_total_average)
    result+="=" * 60+"\n"
    return result

def view_total(user_id) :
    result="=" * 60+"\n"
    total_rank = 1
    total_rank_count = 0
    total_rank_score = 80
    for i in All_Total_table:
        if total_rank_score == i.all_total:
            total_rank_count += 1
        else:
            total_rank_score = i.all_total
            if total_rank_count == 0:
                total_rank_count = 1
            total_rank += total_rank_count
            total_rank_count = 0
        if i.id == user_id:
            result +=str(i)
            result+="총점(가중치 부과)에서 {}등입니다!\n\n".format(total_rank)
            result+="상위 {}%입니다!\n\n".format(round((total_rank / len(All_Total_table)) * 100, 3))
            break

    # 전체 학생 총점 (가중치 부과) 평균
    all_total = 0
    for i in All_Total_table:
        all_total += i.all_total
    all_total_average = all_total / len(All_Total_table)
    result+="전체 학생 총점(가중치 부과) 평균은 {}점입니다.\n".format(round(all_total_average,3))
    result+="=" * 60+"\n"
    return result





