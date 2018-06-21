#Set and tuple
def mating_pairs(males, females):
    pairs = set()
    for a in range(len(males)):
        element = males.pop(), females.pop()
        pairs.add(element)

    return pairs


males = input()  # ex) m1 m2 m3 m4
females = input()  # ex) f1 f2 f3 f4
males_set = set(males.split())
females_set = set(females.split())
pairs = mating_pairs(males_set, females_set)
print(pairs)
# ex) {('m3', 'f3'), ('m1', 'f1'), ('m4', 'f4'), ('m2', 'f2')}

print("="*60)

#Dictionary

def count_values(dictionary):
	# add your code here
	value_count=set(dictionary.values())
	num=len(list(value_count))
	return num


a = dict()
keys = input().split()
values = input().split()
for i in range(len(keys)):
	a[keys[i]] = values[i]

print(count_values(a))

print("="*60)
