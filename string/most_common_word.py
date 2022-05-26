'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

example)

input:
    paragraph = "Bob hit a ball, the hit BALL flew far after it waw hit."
    banned = ["hit"]

output:
    "ball"
'''
from collections import Counter

def find_most_common_word_in_string(input_string: str, banned_words: list[str]) -> str:
    words = input_string.split()
    pure_words = []

    for word in words:
        pure_word = "".join([c.lower() for c in word if c.isalpha]) 
        pure_words.append(pure_word)

    filterd_words = [word for word in pure_words if word not in banned_words]
    word_counter = Counter(filterd_words)

    return word_counter.most_common(1)[0][0]

if __name__ == "__main__":
    print(find_most_common_word_in_string("Bob hit a ball, the hit BALL flew far after it waw hit.", ["hit"]))