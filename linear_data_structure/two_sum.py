'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
'''

# 내 답
def find_indexes_of_two_numbers_when_their_sum_equals_target(num: list[int], target: int) -> list:
    sorted_num = sorted(num)

    for i in range(len(sorted_num)-1):
        for j in range(i, len(sorted_num)):
            if sorted_num[i] + sorted_num[j] == target:
                return [i, j]

    return []
     
# 책 답
# n1 + n2 = target
# -> n2 = target - n1
def two_number(num: list[int], target: int) -> list:
    num_idx_map = {num: idx for idx, num in enumerate(num)}

    for i, n in enumerate(num):
        if ((target - n) in num_idx_map ) and (i != num_idx_map[target-n]):
            return [i, num_idx_map[target-n]]
    
    return []



if __name__ == "__main__":
    print(find_indexes_of_two_numbers_when_their_sum_equals_target([2, 7, 11, 15], 9))
    print(two_number([2, 7, 11, 15], 9))