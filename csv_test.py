import time
import csv
import itertools

with open("username.csv", "r") as file:
    reader = csv.DictReader(file)

    print(dir(reader))

    total = 0
    count = 0
    start_time = time.time()
    first_column = []

    for line in reader:
        # print(line['col1'], line['col2'], line['col2'])
        first_column.append(int(line['col1']))
        total += int(line['col1'])
        count += 1

    print(total / count)
    print(time.time() - start_time)


permutations = itertools.combinations(first_column, 2)
print("wat")
# print(list(permutations))
# print(list(permutations))
our_list = list(permutations)

def mult(list):
    for item in list:
        yield item[0] * item[1]


multiplied = mult(our_list)

print("hey")
print(our_list)
print(our_list)
for output in multiplied:
    print(output)
print("hey")

set = {1,2,2,3}

print(set)

dict = {
    'bob1': 'test1',
    'bob2': 'test2',
    'bob3': 'test3',
}

print(dict['bob2'])

for a,b in enumerate(dict):
    print(b, dict[b], a)

for key, item in dict.items():
    print(key,item)

for i in set:
    print(i)

print(sorted(set, reverse=True))

a=[1,2,3]
a.sort()
print(a)


product = itertools.product("abcd",repeat=2)
print(list(product))

a='abcd'
print(a[::-1])
