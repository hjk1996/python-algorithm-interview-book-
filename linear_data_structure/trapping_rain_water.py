'''
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

example)

-input
    [0,1,0,2,1,0,1,3,2,1,2,1]
-output
    6
'''

# 내 답
def calculate_trapped_rain_volume(heights: list[int]) -> int:
    # 땅의 길이가 2보다 작은 경우 물을 가둘 수 없으므로 0을 반환
    if len(heights) <= 2:
        return 0

    volume = 0
    left_pointer, right_pointer = 0, len(heights)-1
    left_max_idx, right_max_idx = 0, len(heights)-1
    left_max, right_max = 0, 0

    # pointer가 정상 범위 안에 있을 때만
    while (left_pointer < len(heights)) and (right_pointer >= 0): 

        # 좌측에서 탐색
        current_left_max = max(left_max, heights[left_pointer])
        if current_left_max > left_max:
            # 도랑 부피 = 이전 최대 높이 * 이전 최대 높이와 현재 최대 높이 사이에 있는 칸 수 - 사이에 있는 높이 합
            volume += left_max * (left_pointer - left_max_idx - 1) - sum(heights[left_max_idx+1:left_pointer])
            
            left_max = current_left_max
            left_max_idx = left_pointer
        
        # 포인터 이동
        left_pointer += 1

        # 우측에서 탐색
        current_right_max = max(right_max, heights[right_pointer])
        if current_right_max > right_max:
            volume += right_max * (right_max_idx - right_pointer - 1) - sum(heights[right_pointer+1:right_max_idx])

            right_max = current_right_max
            right_max_idx = right_pointer
        
        # 포인터 이동
        right_pointer -= 1
    
    return volume

        
    
if __name__ == "__main__":
    # 땅의 길이가 짝수인 경우
    print(calculate_trapped_rain_volume([0,1,0,2,1,0,1,3,2,1,2,1]))
    # 땅의 길이가 홀수인 경우
    print(calculate_trapped_rain_volume([0,1,0,2,1,0,1,3,2,1,2,1,1]))