from collections import Counter, defaultdict
from typing import List


def anagram_groups_1(arr: List[str]):
    result = []
    while len(arr):
        anagram_group = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if Counter(anagram_group[0]) == Counter(arr[i]):
                anagram_group.append(arr.pop(i))
                continue
            i += 1
        result.append(anagram_group)
    return result


def anagram_groups_2(arr: List[str]):
    result = defaultdict(list)

    for word in arr:
        sorted_word = ''.join(sorted(word))
        result[sorted_word].append(word)

    return list(result.values())


print(anagram_groups_1(["tsar", "rat", "tar", "star", "tars", "cheese"]))
print(anagram_groups_2(["tsar", "rat", "tar", "star", "tars", "cheese"]))