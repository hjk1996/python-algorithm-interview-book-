'''
가장 긴 팰린드롬 부분 문자열을 출력하라.
'''


from time import time

# 함수 실행시간 재는 데코레이터
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        output = func(*args, **kwargs)
        end = time()
        print(end - start)
        return output
    return wrapper

# 내 답
@timer_decorator
def find_longest_palindrome_substring(input_string: str) -> str:

    # 글자가 한 글자거나 전체 문자열이 팰린드롬일 경우 인풋을 그대로 반환함.
    if len(input_string) < 2 or input_string == input_string[::-1]:
        return input_string

    # 윈도우 사이즈 마련
    window_sizes = range(2, len(input_string)+1)

    # 팰린드롬 못찾은 경우 대비
    fall_back = ''

    # 큰 윈도우 사이즈부터 순회
    for window_size in window_sizes[::-1]:
        for i in range(0, len(input_string)-window_size+1):
            # 문자열 윈도우로 슬라이싱
            sliced_word = input_string[i:i+window_size]
            # 큰 윈도우부터 도니까 팰린드롬 찾으면 바로 값 반환
            if sliced_word == sliced_word[::-1]:
                return sliced_word
    
    return fall_back

# 책에 있는 답
@timer_decorator
def find_longest_palindrome_substring2(s: str) -> str:

    def expand(left: int, right: int) -> str:
        # left >= 0 and right < len(s)는 left와 right pointer가 정상 범위 안에 있는지 체크하는 조건문
        # s[left]와 s[right]가 같다면 더 긴 substring 팰린드롬이 있는지 탐색하기 위해 좌우 윈도우를 늘림
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    
    for i in range(len(s)-1):
        # 첫번째 expand는 짝수 팰린드롬 찾기, 두번째 expand는 홀수 팰린드롬 찾기
        result = max(result, expand(i, i +1), expand(i, i + 2), key=len)

    return result


if __name__ == "__main__":
    print(find_longest_palindrome_substring('babad'))
    print(find_longest_palindrome_substring2('babad'))
    print(find_longest_palindrome_substring('bcvioxbusdfioefuddeurtyhtyjgbzasdwe6ui89o7itqeruieryqeuwryhjfghjsdneveroddorevenffsdfgsdfgsdfgfdhjhvhjkhseffuivfhvoauivouadsugjsdfhduiogyuytrtuiowerytwreuitweryut'))
    print(find_longest_palindrome_substring2('bcvioxbusdfioefuddeurtyhtyjgbzasdwe6ui89o7itqeruieryqeuwryhjfghjsdneveroddorevenffsdfgsdfgsdfgfdhjhvhjkhseffuivfhvoauivouadsugjsdfhduiogyuytrtuiowerytwreuitweryut'))