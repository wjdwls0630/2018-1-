user_input=int(input())

b=""
a="*"*user_input
total=0
for i in range(user_input):
    total+=i


    if user_input % 2 != 0:
        if i==int(user_input//2) :
            b+=a+"\n"

        else:
            if i< int(user_input // 2) :
                c = int(user_input // 2)
                d = a[:c].replace("*" * (c-1), " " * (c-1))
                e = a[c+1:].replace("*" * (len(a)-1-(c+1)), " " * (len(a)-1-(c+1)))
                b += d + "*"*total + e + "\n"

            elif i> int(user_input // 2) :
                c = int(user_input // 2)
                d = a[:c].replace("*" * (c-1), " " * (c-1))
                e = a[c + 1:].replace("*" * (len(a)-1-(c+1)), " " * (len(a)-1-(c+1)))
                b += d + "*" * (len(a)-i) + e + "\n"




    else:
        if i==int(user_input//2) :
            b+=a+"\n"

        else:
            if i< int(user_input // 2) :
                c = int(user_input // 2)
                d = a[:c].replace("*" * (c-1), " " * (c-1))
                e = a[c+1:].replace("*" * (len(a)-1-(c+1)), " " * (len(a)-1-(c+1)))
                b += d + "*"*total + e + "\n"

            elif i> int(user_input // 2) :
                c = int(user_input // 2)
                d = a[:c].replace("*" * (c-1), " " * (c-1))
                e = a[c + 1:].replace("*" * (len(a)-1-(c+1)), " " * (len(a)-1-(c+1)))
                b += d + "*" * (len(a)-i) + e + "\n"

print(b)


