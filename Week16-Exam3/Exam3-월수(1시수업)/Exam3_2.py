from math import ceil
user_input=int(input())
a_list=[]
binary_list=[]
if 1<user_input<=2047 :
    a = int(user_input // 2)
    b = int(ceil(user_input % 2))

    a_list.append(a)
    binary_list.append(b)
    while a!=1:
        if a%2==0 :
            a = int(a // 2)
            b=0
            a_list.append(a)
            binary_list.append(b)

        else :
            a = int(a // 2)
            b = 1
            a_list.append(a)
            binary_list.append(b)

        if a==1 :
            binary_list.append(a)
            break
elif user_input==1 :
    binary_list.append(user_input)
elif user_input==2 :

print(a_list)
print(binary_list)
for i in range(len(binary_list)) :
    if binary_list[i]==1 :
        print(i,end=", ")
    elif binary_list[i]==1 and i==range(len(binary_list)) :
        print(i)

