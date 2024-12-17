import re

data = open('input3.txt', 'r').read().split('\n')

def multiplyList(lst):
    return int(lst[0]) * int(lst[1])

string = data[0]


pattern = "mul\(\d\d?\d?,\d\d?\d?\)"
pattern2 = "\d\d?\d?"
pattern_dont = "don't\(\)"
pattern_do = "do\(\)"

x = re.findall(pattern, string)
y = []

for pair in x:
    y.append(re.findall(pattern2, pair))

print("\n")
print(f" Part one Answer: {sum(multiplyList(pair) for pair in y)}")

do_list = []
looking_for = "don't"


while True:
    if looking_for == "don't":
        try:
            obj = re.search(pattern_dont, string)
            do_list.append(string[:obj.start()])
            string = string[obj.end():]
            looking_for="do"
        except:
            break
    if looking_for == "do":
        try:
            obj = re.search(pattern_do, string)
            string = string[obj.end():]
            looking_for="don't"
        except:
            break

if looking_for=="don't":
    do_list.append(string)

part2_multpily_list = []

for string1 in do_list:
    part2_multpily_list.append(re.findall(pattern, string1))

part2_pairs = []
for pair_list in part2_multpily_list:
    for pair in pair_list:
        part2_pairs.append(re.findall(pattern2, pair))


print(f"part 2 answer is: {sum(multiplyList(pair) for pair in part2_pairs)}")

    












