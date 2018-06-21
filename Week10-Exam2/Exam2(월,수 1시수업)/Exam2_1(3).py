filename = input('Enter the filename: ')
file = open(filename, 'r')
file.readline()
data = file.readline()
while data.startswith('#'):
    data = file.readline()

data = data.strip().split()
for data in file:
    for i in data:
        if data == '-':
            data.remove('-')
i = 0
for i in data:
    if int(i) < int(data[i]):
        i = int(i)
    else:
        i = int(data[i])

print(i)

