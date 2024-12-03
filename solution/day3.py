data_path = r'../data/day3.txt'

total = 0

for l in open(data_path):
    line = l.strip()

    muls = line.split('mul(')

    for mul in muls:

        if ')' not in mul:
            continue

        nums = mul.split(')')[0]

        if ',' not in nums:
            continue

        nums = nums.split(',')

        try:
            num1 = int(nums[0])
            num2 = int(nums[1])
        except ValueError:
            continue

        total += num1 * num2

print(total)




