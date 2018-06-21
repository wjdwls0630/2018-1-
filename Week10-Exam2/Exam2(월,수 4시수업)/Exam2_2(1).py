# do not modify the lists
eng_score =  [100, 80, 94, 50, 74, 35]
math_score = [90, 60, 97, 35, 65, 62]
prog_score = [95, 70, 100, 60, 80, 43]


# implement here
def get_avg_median(l1,l2,l3) :
    avg_score=[]
    for i in range(len(l1)):
        result=round((l1[i] + l2[i] + l3[i])/3,2)
        avg_score.append(result)
    avg_score.sort()

    median_score=avg_score[int(len(avg_score)/3)+1]

    return avg_score, median_score




# do not modify the main body
eng_score.append(int(input()))  #"Enter the Englsih score: "
math_score.append(int(input())) #"Enter the math score: "
prog_score.append(int(input())) #"Enter the programming score: "
avg_score, median_score = get_avg_median(eng_score, math_score, prog_score)
print("average score:", avg_score)
print("median score:", median_score)
