file = open("data/BIG_MAC_INDEX.txt", "r")

lines = file.readlines()
data = []
for line in lines:
    if not line.startswith("#"):
        data.append(line.strip())

file.close()


a_data = []
b_data = []
a_total = 0
b_total = 0
for element in data[:6]:
    
    name,price =element.split(", ")
    if price.startswith('$') :
        price = float(price[1:])
        
        a_data.append(price)
        a_total = a_total + price


for element in data[6:]:
    
    name,price =element.split(", ")
    if price.startswith('$') :
        price = float(price[1:])
        
        b_data.append(price)
        b_total = b_total + price


a_avg = round(a_total / 6, 2)
b_avg = round(b_total / 6, 2)

print("Six the most expensive BMIs: ", a_data, "(Avg: {})".format(a_avg))
print("Six the cheapest BMIs: ", b_data, "(Avg: {})".format(b_avg))


