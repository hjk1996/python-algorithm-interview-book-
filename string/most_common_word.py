'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
'''

from collections import Counter

def find_most_common_word(input_string: str, banned_words: list[str]) -> str:
    word_list = [word.lower() for word in input_string.split()]
    banned_words = [word.lower() for word in banned_words]
    processed_word_list = []

    for word in word_list:
        processed_word = "".join([c for c in word if c.isalpha()])
        processed_word_list.append(processed_word)
    
    processed_word_list = [word for word in processed_word_list if word not in banned_words]

    counter = Counter(processed_word_list)
    print(counter.most_common(1)[0][0])

if __name__ == "__main__":
    find_most_common_word("Bob hit a ball, the BALL flwe far after it was hit.", banned_words=["hit"])