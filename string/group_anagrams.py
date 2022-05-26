from collections import Counter
from collections import defaultdict


def group_anagrams(input_anagrams: list[str]) -> None:
    grouped_anagram_map = defaultdict(list)
    for word in input_anagrams:
        counter = Counter(word)
        sorted_counter = tuple(sorted(tuple(counter.items())))
        grouped_anagram_map[sorted_counter].append(word)
    
    print([value for key, value in grouped_anagram_map.items()])

if __name__ == "__main__":
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])