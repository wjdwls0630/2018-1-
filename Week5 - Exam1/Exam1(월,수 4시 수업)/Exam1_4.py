
age = int(input())
sex = input()
def function(sex,age) :
    if sex == "M" or sex == "m":
        if 0 <= age < 10:
            result="water"
        elif 10<=age < 30:
            result ="beer"
        elif 30<=age < 80:
            result ="soju"
        elif age >= 80:
            result ="rice"
        else:
            result ="fail1"
        return result
    elif sex == "w" or sex == "W":
        if 0 <= age < 10:
            result ="apple"
        elif 10<=age < 30:
            result ="pasta"
        elif 30<=age < 80:
            result ="steak"
        elif age >= 80:
            result ="rice"
        else:
            result ="fail1"
        return result
    else:
        if age >= 0:
            result ="fail2"
        else:
            result ="fail1\nfail2"
        return result

print(function(sex,age))