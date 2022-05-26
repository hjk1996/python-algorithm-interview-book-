# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# *팰린드롬: 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어

def is_palindrom(input_string: str) -> bool:
    processed_string_list = [c.lower() for c in input_string if c.isalnum()]
    return processed_string_list == processed_string_list[::-1]


print(is_palindrom("A man, a plan, a canal: Panama"))
print(is_palindrom("race a car"))