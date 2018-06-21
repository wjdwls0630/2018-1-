file=open('myin.txt','r')
avg_list=[]
for line in file :
	a=line.split()
	total=0	
	for j in a :
		k=int(j)
		total=total+k
	avg=total/len(a)
	avg_list.append(avg)
	print(avg)
print("max=",max(avg_list))
print("min=",min(avg_list))

