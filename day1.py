from functools import reduce

data = open('input.txt', 'r').read().split('\n')


left_list = []
right_list = []
found_in_counts = []

for pair in data:
    left_list.append(int(pair[0:5]))
    right_list.append(int(pair[8:]))

for value in left_list:
    found_in_counts.append((value, right_list.count(value)))

x = []

for value, count in found_in_counts:
    if count == 0:
        pass
    else:
        x.append(value*count)

print(sum(x))


