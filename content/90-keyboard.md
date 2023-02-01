+++
title = "Designing a keyboard layout"
slug = "keyboard"
date = 2023-01-13
draft = true
+++

During the summer of 2017, I designed an alternative keyboard layout to enhance my typing experience. This is what I came up with:

![bold layout](/images/bold_layout.png)

I also remapped caps-lock to act as a secondary layer with additional functionality:

![bold layout](/images/bold_alt.png)

- Arrow keys, `home`, and `end` on the homerow for easy navigation (compatible with shift and option modifiers)
- Select line / word under cursor
- Delete
- macOS function keys along the number row for controlling brightness, volume, and media (circumventing mbp touchbars 🤮)

The extra layer provides massive benefit to effort ratio. The rest of the blog post describes the keyboard layout but I'd recommend at least trying to build your own custom layer. This extra layer makes it effortless to jump around text and code without leaving the homerow. Combined, these transformations have offered me a pleasant typing experience which I continue to use to this day.

The functionality is enabled by the excellent [Karabiner-Elements](https://karabiner-elements.pqrs.org) application on macOS and [AutoHotkey](https://www.autohotkey.com) on Windows. You can find my configuration files for these respective tools in my [dotfiles repository](https://github.com/chariotsofiron/dotfiles).

# Why?



My goal is comfort, not speed.

A month of getting back to your old speeds for a lifetime of just enjoying typing more is worthwhile if you're at your computer a lot.

As a developer 

Is it worth it? I type _a lot_. I anticipate that I will be typing for many years into the future. By [XKCD #1205](https://xkcd.com/1205/) I think it's worth it.


I never learned how to type "touch-type" properly resting my fingers along the homerow. I had heard about other alternative all my fingers. 
I figured since I type so much, it would be worthwhile to learn correct techniqued. As I embarked on the task, I learned about "alternative keyboard layouts" such as Dvorak and Colemak. Since I was already relearning how to type, I thought I should learn a new layout at well.
And I humbly thought I could do better...
Although some people are able to type fast using only [2 fingers](https://youtu.be/GgUcXRby3zc?t=1015).


# Comfort

The major factors influencing typing comfort include physical key placement, key layout (location of letters relative to each other), and typing method.

[Touch-typing](https://en.wikipedia.org/wiki/Touch_typing) is a method of typing where the eight fingers are placed in a horizontal row along the middle of the keyboard (the home row) and having them reach for other keys. With the QWERTY keyboard layout, some words are harder to type than others, such as trimmingly, orthotics, suburban, assuming. Meanwhile, other words such as area, people, were are easier.

Many words on QWERTY are uncomfortable to touch-type. Many people develop a hybrid style of typing, a mixture of touch-typing and the hunt-and-peck approach. More can be read about hybrid typing in this [article](https://phys.org/news/2016-02-ten-fingers-fast.html).

Peddlers of typing classes might claim that touch-typing increases speed, but individuals can type comfortably using as few as two fingers [using two fingers](https://youtu.be/GgUcXRby3zc?t=1015)

QWERTY often causes uncomfortable contortions. It's no wonder so many people learn hybrid approaches, or learn to type comfortably .

Many people report wrist pain that gets alleviated after switching to a different keyboard layout. Using an ergonomic keyboard likely helps just as much.

This leads to some natural questions:
- What makes a motion comfortable or uncomfortable?
- How can we quantify quantify comfort?
- Can we design a keyboard layout that maximizes comfort?

# Defining terms

Bigrams are a sequence of two consecutive letters, "th". Trigrams are three consecutive letters, "the".

The movements we trace with our fingers when typing can be divided into several categories:
- Hand alternation: typing the next key with the opposite hand you last used
- Same finger repetition: type two keys consecutively with the same finger
- Rolls: type 2-3 keys with one hand in the same direction (inward or outward)
- Roll ratio: proportion of inward vs outward rolls
- Zig-zag motions: change direction when typing a trigram
- Row jumps: e.g. `cr` on QWERTY

# Goals

The next part of the exercise is selecting which metrics we'd like to optimize. This part is quite subjective. For me personally:
- Heatmap proportional to how easy it is to type
- Maximize hand alternation (bigrams typed with both hands). Gives time for you to set up your finger while typing the other key.
- Maximize inward rolls ("rolling" your fingers towards the center of the keyboard when typing). I find inward rolls more comfortable than outward rolls, but some people feel indifferent
- Minimize same finger repetition (bigrams typed with the same finger)
- Minimize seesaw motions (trigrams that consist of one inward and outward motion)
- Minimize row jumps

Balancing these characteristics is a bit of an art and certainly more subjective. 

- Great for programming and Vim
- Fixed zxcv. A lot of people care about this.
- High hand alternation
- high inward rolls


# Existing layouts

In 2017, there were a few people that had explored this problem. Dvorak and Colemak had existed for a while, and some people had tried making their own layouts.

I spent some time studying and learning these layouts, and it seemed like there was no software to evaluate how good they were, so I made my own.


Dvorak
- outward rolls


Colemak
- seesaw motions


# Layout statistics


```
BOLD            228.752 total effort   108.234 positional effort    left right
                  1.409 same finger rp  15.611 shift same finger top 12.9 10.6
bldfw/,oyk       70.374 hand alternat.  27.617 shift hand alter. mid 30.3 33.9
rnstmuaeih        3.648 inward/outward  25.638 inward or outward bot  7.2  5.2
zxcvg;.qjp       11.186 adjacent        12.905 shift adjacent    sum 50.4 49.6
                  5.504 no hand altern. 43.392 two hand altern.
                  2.889 seesaw           6.209 indir same finger
                8.5 10.9 13.3 17.7 --.- --.- 12.8 18.8  8.8  9.2 Sh  1.1  1.7
same fing/fi.  0.14 0.07 0.31 0.25           0.33 0.13 0.05 0.12 Sh 2.3913.22
" " jump >= 2  0.00 0.00 0.00 0.00           0.02 0.00 0.00 0.00 Sh 0.23 0.02
adjacent/fin.pair 0.52 2.80 2.28                2.48 1.88 1.24   Sh 7.40 5.51
" " row jump >=2  0.01 0.15 0.05                0.02 0.05 0.02   Sh 1.68 0.64
```

# Learning the layout

My goal was to get back up to 100WPM which I find to be a very comfortable speed for productivity.

- keybr to learn the layout
- typingcat
- typing test


# FAQ

1. **Can I still type in QWERTY?** Yes. Because I never did learn how to properly type in qwerty, the muscle memory doesn't overlap much and I can still type ~80wpm
2. **What keyboard do I use?** Current Anne Pro 2



------



# Corpus

- vim, english, bigram/trigram frequency
- Colemak has a 50/50 
- https://mdickens.me/typing/theory-of-letter-frequency.html


# Qwerty
As mentioned in https://en.wikipedia.org/wiki/QWERTY#Properties, the QWERTY layout was likely designed to prevent typewriter jamming and speed.
Even the staggered layout is a remnant of the typewriter baggage. Some communities have devised "orthogonal" layouts where the keys are placed in a grid.



## Implementing in software


I tried learning Dvorak, and then colemak, getting up to 50wpm in each. (inb4 "you shoulda stuck it out longer before realizing the true benefits")
If I was going through all the trouble of learning to type properly, I thought I might use a new keyboard layout.


A lot of people think about speed when considering a different keyboard layout. I think the more interesting value proposition is comfort, and speed follows from that.

I found a german program called for analyzing keyboard layouts [ADNW](http://www.adnw.de/)

Dvorak has high hand alternation



## Recreate the environment

```bash
g++ -std=c++11 -O2 -DNDEBUG -DENGLISH -DTASTENZAHL=33 opt.cc -o opt
```


```javascript
QWERTY          443.611 total effort   184.951 positional effort    left right
                  6.800 same finger rp   5.990 shift same finger top 28.0 20.2
qwertyuiop       52.758 hand alternat.  41.713 shift hand alter. mid 22.1  9.6
asdfghjkl;        1.073 inward/outward  37.864 inward or outward bot  6.8 13.3
zxcvbnm,./       21.605 adjacent        11.942 shift adjacent    sum 56.9 43.1
                  25.289 no hand altern. 27.150 two hand altern.
                  13.192 seesaw           5.655 indir same finger
                9.1  8.4 18.5 20.9 --.- --.- 18.4  8.9 12.1  3.7 Sh  1.1  1.7
same fing/fi.  0.04 0.07 2.96 1.59           1.16 0.22 0.75 0.01 Sh 5.60 0.39
" " jump >= 2  0.00 0.00 1.03 0.21           0.87 0.01 0.02 0.00 Sh 0.00 0.38
adjacent/fin.pair 1.82 3.19 8.74                4.79 2.22 0.84   Sh 0.6411.30
" " row jump >=2  0.00 0.22 2.21                3.48 0.03 0.03   Sh 0.06 7.98


COLEMAK         241.001 total effort   104.325 positional effort    left right
                  1.358 same finger rp  13.653 shift same finger top  7.8  8.3
qwfpgjluy;       58.113 hand alternat.  40.206 shift hand alter. mid 32.7 37.3
arstdhneio        1.034 inward/outward  37.951 inward or outward bot  6.8  7.3
zxcvbkm,./       17.487 adjacent         8.548 shift adjacent    sum 47.2 52.8
                  16.768 no hand altern. 30.773 two hand altern.
                  10.561 seesaw           5.575 indir same finger
                9.1  7.8 11.6 18.7 --.- --.- 18.8 15.4  9.8  8.8 Sh  1.1  1.7
same fing/fi.  0.04 0.04 0.17 0.18           0.39 0.37 0.16 0.01 Sh 5.06 8.59
" " jump >= 2  0.00 0.00 0.00 0.00           0.07 0.00 0.11 0.00 Sh 0.05 0.01
adjacent/fin.pair 2.30 1.03 2.47                9.34 1.35 0.99   Sh 3.09 5.46
" " row jump >=2  0.00 0.00 0.00                0.27 0.16 0.00   Sh 0.07 0.51


DVORAK          260.778 total effort   125.364 positional effort    left right
                  2.679 same finger rp  12.404 shift same finger top  6.0 16.8
/,.pyfgcrl       70.460 hand alternat.  34.504 shift hand alter. mid 36.1 30.4
aoeuidhtns        1.598 inward/outward  24.282 inward or outward bot  3.0  7.6
;qjkxbmwvz       11.122 adjacent        19.795 shift adjacent    sum 45.1 54.9
                  5.501 no hand altern. 44.775 two hand altern.
                  2.971 seesaw           5.847 indir same finger
                9.7  8.3 13.0 14.1 --.- --.- 16.5 13.3 13.7 11.4 Sh  1.8  0.9
same fing/fi.  0.02 0.03 0.22 0.97           0.43 0.48 0.31 0.23 Sh 9.46 2.95
" " jump >= 2  0.00 0.00 0.00 0.09           0.01 0.00 0.05 0.01 Sh 0.01 1.68
adjacent/fin.pair 0.10 0.44 2.45                4.50 2.51 1.12   Sh11.93 7.87
" " row jump >=2  0.00 0.00 0.02                0.01 0.04 0.03   Sh 0.16 2.12
```



## Inspiration

- https://xsznix.wordpress.com/2016/05/16/introducing-the-rsthd-layout/
- https://www.jonashietala.se/blog/2021/06/03/the-t-34-keyboard-layout/
- https://www.reddit.com/r/Norman/wiki/index#
- https://en.wikipedia.org/wiki/Touch_typing

- https://geekhack.org/index.php?topic=67604.0
- http://www.adnw.de

Servers
This server - https://discord.gg/2qq8qmDtFf
This server on matrix - https://matrix.to/#/!iZdsjIZXWPXnohYGdD:matrix.org
Dvorak - https://discord.com/invite/JXpsSR2
Colemak - https://discord.gg/3VsHDG86hM
ColemaQ - https://discord.gg/Csra5jK2R6
Monkeytype - https://discord.gg/FcjrA7pBpG
Babymak (not a joke) - https://discord.gg/frtQHGrNwm

Resources
Keyboard Layouts Doc - Many known layouts compiled in one place, sorted by SFB rate | https://bit.ly/keyboard-layouts-doc
Dreymar's Big Bag - A collection of modifications and other useful tricks | https://dreymar.colemak.org/
SteveP Analyzer - A good fork of the patorjk layout analyzer | https://stevep99.github.io/keyboard-layout-analyzer/#/main
Mod DH Analyzer - A detailed and configurable layout analyzer | https://colemakmods.github.io/mod-dh/analyze.html 
CarpalX - The original layout analyzer and generator | http://mkweb.bcgsc.ca/carpalx/ 
gfruit's Words Filter - A simple yet incredibly useful tool for finding words with certain bigrams, characters, and fingers | https://gfruit.github.io/typing/words-filter.html
Octa's Keymap Creator- A tool for creating and sharing layout fingermaps | https://keymap-creator--octatypes.repl.co/ 
Monkeytype Fingermap - Same as above, made by the creator of MonkeyType | https://fingermap.monkeytype.com/
genkey - Layout analyzer and generator CLI | https://semilin.github.io/genkey
a200 - A spreadsheet-like layout analyzer | https://github.com/ClemenPine/200-analyzer
https://news.ycombinator.com/item?id=23400058

- [Canary Keyboard Layout](https://github.com/Apsu/Canary)
- [Workman Keyboard Layout (2010)](https://workmanlayout.org/)



https://docs.google.com/document/d/1_a5Nzbkwyk1o0bvTctZrtgsee9jSP-6I0q3A0_9Mzm0/edit#
https://github.com/Apsu/Canary
https://semilin.github.io



Macros
- https://getreuer.info/posts/keyboards/macros/
- https://getreuer.info/posts/keyboards/select-word/index.html
- karabiner
  - https://github.com/pqrs-org/Karabiner-Elements/issues/2532
  - https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/conditions/variable/