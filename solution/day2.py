import csv

data_path = r'../data/day2.txt'


def read_data(data_path):
    with open(data_path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        data = list(reader)
    return data


data = read_data(data_path)


def get_stats(row):
    nums = [int(num) for num in row]
    for i, num in enumerate(nums):
        if i == len(nums) - 1:
            continue

        nums[i] -= nums[i + 1]

    nums = nums[:-1]

    if any(abs(num) > 3 for num in nums):
        return False

    if all(num < 0 for num in nums):
        return True

    if all(num > 0 for num in nums):
        return True

    return False


statuses = [get_stats(row) for row in data]

print(sum(statuses))
