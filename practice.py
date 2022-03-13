import itertools
import csv

exampleFile = open('username.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData[0])
print(exampleReader)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

print("test")

outputFile = open('test.csv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter=';')
outputWriter.writerow(['spam', 'eggs', 'bacon', 'test'])
outputWriter.writerow(['Hello world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

import csv
exampleFile = open('username.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['spam'], row['eggs'], row['bacon'], row['hey'])


import csv
with open('username.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # output = []

    output = [row['col1'] for row in csv_reader]

    # with open('test.csv','w') as new_file:
    #     fieldnames = ['col1','col2']
    #     csv_writer = csv.DictWriter(new_file, delimiter='-', fieldnames= fieldnames)
    #     csv_writer.writeheader()
    #     for line in csv_reader:
    #         del line['col3']
    #         csv_writer.writerow(line)

    for row in csv_reader:
        output.append(row['col1'])
        # print(row['spam'], row['eggs'], row['bacon'], row['hey'])

    print(output)

import csv
file = open('test.csv', 'w', newline='')
writer = csv.DictWriter(file, ['col1','col2','col3'])
writer.writeheader()
writer.writerow({'col1': 'Alice', 'col2': 'cat', 'col3': '555-1234'})
file.close()

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))

print(sum_of_first_n)


counter = itertools.repeat(2, times=3)

for i in counter:
    print(i)
print(next(counter))
print(next(counter))
print(next(counter))

x = [i ** 2 for i in range(10)]
print(x)


def lenfunc(n):
    return n+1

squares = map(pow, range(10), itertools.repeat(2))
squraes2 = itertools.starmap(pow, [(0,2),(1,2),(2,2)])

print(list(squares))
print(list(squraes2))

letters = ['a','b','c','d']
result = itertools.permutations(letters, 2)
# for item in result:
#     print(item)

print(len(list(result)))

# numbers1 = [1,2,3,4]
# numbers2= [5,6,7,8]


# combined = itertools.chain(numbers1, numbers2)
# print(list(combined))
# iter = (i for i in range(50))
# print(sum(1 for _ in iter))

# slice = itertools.islice(range(10), 1, 5, 2)
# print(list(range(10)))

# for item in slice:
#     print(item)

# selectors = [True, False, True, False]
# result = itertools.compress(letters, selectors)

# for item in result:
#     print(item)

# def lt_2(n):
#     return n<2

# result = filter(lt_2, numbers1)
# print(list(result))
