+++
title = "Watsky words"
+++

Between 2019 and 2023, rapper George Watsky released three albums titled Complaint, Placement, and Intention. When arranged next to each other, the titles form a 3x3 word puzzle that can be read across and down:

```
com pla int
pla cem ent
int ent ion
```

In an [interview with Philip DeFranco](https://www.youtube.com/watch?v=6pDUCAgsnKU&t=2562s), Watsky said the following:

> when I worked with this linguist, we plugged the rules of this word puzzle into the english dictionary and it only spit out one possibility of 9-letter words that interlocked in the way we wanted it to...there was only one solution

Let's double check their work. We start with a list of english words and filter it down to words with 9 letters:

```shell
$ curl https://raw.githubusercontent.com/chariotsofiron/words/main/words.txt
    | rg -o '^[a-z]{9}\b'
    | sort > words.txt
$ wc -l words.txt
    12246 words.txt
```

Checking all three-word combinations of that list would take a long time ($12246^3=1,836,465,462,936$). We can explore the search space more efficiently by using binary search to find the words with the prefix we want:

```python
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

```

Running this gives us 490 solutions:

```shell
$ python3 watsky.py | rg -c '^-'
490
```

Some of the other album titles Watsky could have chosen include:

```
worshiped
shittiest
pedestals

castrates
traumatic
testicles

prostates
statistic
testicles
```

I think these would have been equally interesting.
