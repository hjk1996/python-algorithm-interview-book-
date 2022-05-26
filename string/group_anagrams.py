'''
문자열 배열을 받아 애너그램 단위로 그루핑하라.
*애너그럼: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
'''


from collections import Counter
from collections import defaultdict


# 내 풀이
def group_anagrams(input_anagrams: list[str]) -> None:
    grouped_anagram_map = defaultdict(list)
    for word in input_anagrams:
        counter = Counter(word)
        sorted_counter = tuple(sorted(tuple(counter.items())))
        grouped_anagram_map[sorted_counter].append(word)
    
    print([value for key, value in grouped_anagram_map.items()])

# 정석 풀이
def group_anagrams(input_anagrams: list[str]) -> None:
    anagrams = defaultdict(list)

    for word in input_anagrams:
        # 문자열을 정렬해서 넣으면 같은 애너그램을 그룹지을 수 있음.
        anagrams[''.join(sorted(word))].append(word)

    print(anagrams.values())

if __name__ == "__main__":
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])