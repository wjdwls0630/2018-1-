#do not modify "veg" list
veg_list = ["배추", "상추", "수박"]
user=input()
if user in veg_list :
	veg_list.remove(user)
else :
	veg_list.append(user)
print(veg_list)