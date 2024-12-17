from functools import cache
#checks a list of stones
#if 0 make it one
#if digits lengh == even spilt in half into two sperate
    #if new number has leading 0s remove leading zeros
#else mutiple number by 2024output lengh of new stone list

stones = [2, 77706, 5847, 9258441, 0, 741, 883933, 12]
'''
def blink(stones):
    new_stones_list = []

    for value in stones:
        if value == 0:
            new_stones_list.append(1)
        elif len(str(value))%2 == 0:
            new_stones_list.append(int(str(value)[0:int(len(str(value))/2)]))
            new_stones_list.append(int(str(value)[int(len(str(value))/2):]))
        else:
            new_stones_list.append(value*2024)
    return new_stones_list

         

for i in range(75):
    print(f"loading...{i}")
    stones = blink(stones)
print(f"The Stone lengh will be............ {len(stones)}")


'''

@cache
def count(stone, steps):
    if steps == 0:
        print(f"I am the last stone----- {stone}    On Step...... {steps}")
        return 1
    if stone == 0:
        print(f"Step: {steps}   Stone Number: {stone}  stone set to 1")
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length%2 ==0:
        print(f"Step: {steps}   Stone Number: {stone}   Stone SPLItING")
        return count(int(string[0:length//2]), steps - 1) + count(int(string[length//2:]), steps - 1)
    print(f"Step: {steps}   Stone Number: {stone}  stone getting big")
    return count(stone * 2024, steps - 1)
    


print(sum(count(stone, 75) for stone in stones))





    


