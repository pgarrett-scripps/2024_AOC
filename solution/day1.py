import csv

data_path = r'../data/day1.txt'


def read_data(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        data = list(reader)
    return data


data = read_data(data_path)

list1, list2 = [], []
for row in data:
    list1.append(int(row[0]))
    list2.append(int(row[3]))

list1.sort()
list2.sort()

list_diff = [abs(list1[i] - list2[i]) for i in range(len(list1))]
print(sum(list_diff))
