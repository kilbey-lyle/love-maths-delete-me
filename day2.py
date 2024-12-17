data = open('input2.txt', 'r').read().split('\n')

levels = []

for level in data:
    levels.append(level.split(" "))





def sortingIsCorrect(level):
    int_level = list(map(int, level))
    sorted_up = sorted(int_level)
    sorted_down = sorted(int_level, reverse=True)
    if int_level == sorted_up:
        return True 
    elif int_level == sorted_down:
        return True
    return False

def noLargeGaps(level):
    right_answers = [1, -1, 2, -2, 3, -3]
    diffs = [abs(int(a)-int(b)) for a, b in zip(level, level[1:])]
    for num in diffs:
        if num not in right_answers:
            return False
    return True

def isSafe(level):
    sorting_safe = sortingIsCorrect(level)
    gaps_safe = noLargeGaps(level)
    return gaps_safe and sorting_safe
    

safe_count = sum(isSafe(level) for level in levels)
print(f"print safe count: {safe_count}")

safe_count_pt2 = 0
for level in levels:
    safe = False
    print("=====")
    for i in range(len(level)):
        level_ommiting_a_floor = level[:i]+level[i+1:]
        print(level_ommiting_a_floor)
        if isSafe(level_ommiting_a_floor):
            safe = True
    if safe:
        safe_count_pt2 += 1

print(f"print safe count part 2 : {safe_count_pt2}")

