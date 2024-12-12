from itertools import islice
#checks a list of stones
#if 0 make it one
#if digits lengh == even spilt in half into two sperate
    #if new number has leading 0s remove leading zeros
#else mutiple number by 2024output lengh of new stone list

stones = [2, 77706, 5847, 9258441, 0, 741, 883933, 12]

def blink(stones):
    new_stones_list = []

    for value in stones:
        if value == 0:
            new_stones_list.append(1)
        elif len(str(value))%2 == 0:
            second_half_index_start_ponit = int(len(str(value))/2)
            value_list = [digit for digit in str(value)]
            first_half = ''.join(value_list[0:second_half_index_start_ponit])
            second_half = ''.join(value_list[second_half_index_start_ponit:])
            new_stones_list.append(int(first_half))
            new_stones_list.append(int(second_half))
        else:
            new_stones_list.append(value*2024)
    return new_stones_list

         
def workout_stone_lengh(num, values):
    new_stones= []
    for i in range(num):
        print(f"loading...{i}")
        new_stones = blink(values)
        values = new_stones
    print(f"The Stone lengh will be............ {len(new_stones)}")


workout_stone_lengh(75, stones)
            
            
            
    


