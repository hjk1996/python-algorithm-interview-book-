'''
가장 긴 팰린드롬 부분 문자열(substring)을 출력하라

example)

-input:
    "babad"
-output:
    "bab"
'''

def find_longest_palindrome_substring(input_string: str) -> str:
    
    def expand(left: int, right: int) -> str:
        while (left >= 0 and right < len(input_string)) and (input_string[left] == input_string[right]):
            left -= 1
            right += 1

        return input_string[left+1:right]

    result = ""

    for i in range(len(input_string)):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result  

if __name__ == "__main__":
    print(find_longest_palindrome_substring("babad"))