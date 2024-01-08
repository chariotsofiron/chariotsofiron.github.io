from bisect import bisect_left
from itertools import takewhile
from typing import Iterator


def starts_with(words: list[str], prefix: str) -> Iterator[str]:
    left = bisect_left(words, prefix)
    return takewhile(lambda word: word.startswith(prefix), words[left:])


words = open("words.txt").readlines()
for first in words:
    for third in starts_with(words, first[6:]):
        for second in starts_with(words, first[3:6]):
            if second.endswith(third[3:6]):
                print("-" * 9)
                print(first)
                print(second)
                print(third)
