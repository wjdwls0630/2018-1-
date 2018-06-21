# do not modify 'rep_list' and 'no_att_list'
rep_list = [["Prior", "Trump", "Powell"],
            ["Kim", "Moon", "Lee"],
            ["Wang", "Xi", "Li"]]

no_att_list = ["Prior", "Lee", "Li"]

no_att_name = input()
no_att_list.append(no_att_name)


for name in no_att_list :
    for i in rep_list :
        for j in i :
            if j==name :
                i.remove(name)


print("Attendants:")
for i in rep_list :
    name_str="\t"
    for j in i :
        name_str+=j+","
    print(name_str)

