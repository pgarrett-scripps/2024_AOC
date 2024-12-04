data_path = r'../data/day4.txt'

"""
Part 1
"""

lines = []
for l in open(data_path):
    line = l.strip()
    lines.append(line)

xmas_count = 0

for line in lines:
   xmas_count += line.count('XMAS')
   xmas_count += line[::-1].count('XMAS')

transposed_lines = ['' for _ in range(len(lines[0]))]
for i in range(len(lines[0])):
    for line in lines:
        transposed_lines[i] += line[i]

for line in transposed_lines:
   xmas_count += line.count('XMAS')
   xmas_count += line[::-1].count('XMAS')

diagonal_lines = []
for i in range(len(lines[0])):
    diagonal_lines.append('')
    for j in range(0, len(lines)):
        if i+j >= len(lines[0]):
            break
        diagonal_lines[-1] += lines[j][i+j]

for i in range(len(lines[0])-2, 0, -1):
    diagonal_lines.append('')
    for itr, j in enumerate(range(len(lines[0])-1, 0, -1)):
        if i-itr < 0:
            break
        diagonal_lines[-1] += lines[j][i-itr]

for i in range(len(lines[0])):
    diagonal_lines.append('')
    for j in range(0, len(lines)):
        if i+j >= len(lines[0]):
            break
        diagonal_lines[-1] += lines[::-1][j][i+j]

for i in range(len(lines[0])-2, 0, -1):
    diagonal_lines.append('')
    for itr, j in enumerate(range(len(lines[0])-1, 0, -1)):
        if i-itr < 0:
            break
        diagonal_lines[-1] += lines[::-1][j][i-itr]

for line in diagonal_lines:
   xmas_count += line.count('XMAS')
   xmas_count += line[::-1].count('XMAS')


"""
Part 2
"""

xmas_count = 0

conv = [(0,0), (0,2), (1,1), (2,0), (2,2)]
conv_values = ['M', 'S', 'A', 'M', 'S']
for i in range(len(lines)):
    for j in range(len(lines[0])):
        conv_flag = True
        for c, v in zip(conv, conv_values):
            c_adj = (i+c[0], j+c[1])

            if c_adj[0] >= len(lines) or c_adj[1] >= len(lines[0]):
                conv_flag = False
                break

            if lines[c_adj[0]][c_adj[1]] != v:
                conv_flag = False
                break

        if conv_flag:
            xmas_count += 1

conv_values = ['S', 'S', 'A', 'M', 'M']
for i in range(len(lines)):
    for j in range(len(lines[0])):
        conv_flag = True
        for c, v in zip(conv, conv_values):
            c_adj = (i+c[0], j+c[1])

            if c_adj[0] >= len(lines) or c_adj[1] >= len(lines[0]):
                conv_flag = False
                break

            if lines[c_adj[0]][c_adj[1]] != v:
                conv_flag = False
                break

        if conv_flag:
            xmas_count += 1

conv_values = ['S', 'M', 'A', 'S', 'M']
for i in range(len(lines)):
    for j in range(len(lines[0])):
        conv_flag = True
        for c, v in zip(conv, conv_values):
            c_adj = (i+c[0], j+c[1])

            if c_adj[0] >= len(lines) or c_adj[1] >= len(lines[0]):
                conv_flag = False
                break

            if lines[c_adj[0]][c_adj[1]] != v:
                conv_flag = False
                break

        if conv_flag:
            xmas_count += 1

conv_values = ['M', 'M', 'A', 'S', 'S']
for i in range(len(lines)):
    for j in range(len(lines[0])):
        conv_flag = True
        for c, v in zip(conv, conv_values):
            c_adj = (i+c[0], j+c[1])

            if c_adj[0] >= len(lines) or c_adj[1] >= len(lines[0]):
                conv_flag = False
                break

            if lines[c_adj[0]][c_adj[1]] != v:
                conv_flag = False
                break

        if conv_flag:
            xmas_count += 1

print(xmas_count)


