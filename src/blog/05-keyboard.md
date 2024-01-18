# Designing an alternative keyboard layout

Written: 2024-01-13

During the summer of 2017, I designed the following alternative keyboard layout to enhance my typing experience:

![layout](/assets/layout/layout.png)

While working as a software engineer during my first internship, it dawned on me that I would doing a lot of typing for the rest of my life. I had heard of alternative keyboard layouts and it seemed like a good opportunity  I never learned how to touch-type and had heard of alternative keyboard layouts, so this seemed like a good opportunity to feed two birds with one scone.


## Background

The arrangement of letters on a typical US keyboard is called [QWERTY](https://en.wikipedia.org/wiki/QWERTY). When touch-typing, some words are harder to type than others. This can be observed in typing tests for the 50 [slowest](https://10fastfingers.com/text/208691-50-slowest-words-on-QWERTY) and [fastest](https://10fastfingers.com/text/208390-Sean-s-50-Fastest-QWERTY-Words) words.

Alternative keyboard layouts optimize the positions of the letters on a keyboard by considering which words are typed most frequently. The two most popular alternative layouts are Dvorak and Colemak, but the creators did not have the same amount of computing power as we do today.

Since I designed my layout in 2017, a sizeable community has formed around AKLs and have developed several layout analyzers and generators. I'll add some links at the end.


## Language statistics

Words can be broken up into individual letters, bigrams, and trigrams. The 26 most common according to research by [Peter Norvig](https://norvig.com/mayzner.html) are:


| letter | bigram | trigram |
| ------ | ------ | ------- |
| e      | th     | the     |
| t      | he     | and     |
| a      | in     | ing     |
| o      | er     | ion     |
| i      | an     | tio     |
| n      | re     | ent     |
| s      | on     | ati     |
| r      | at     | for     |
| h      | en     | her     |
| l      | nd     | ter     |
| d      | ti     | hat     |
| c      | es     | tha     |
| u      | or     | ere     |
| m      | te     | ate     |
| f      | of     | his     |
| p      | ed     | con     |
| g      | is     | res     |
| w      | it     | ver     |
| y      | al     | all     |
| b      | ar     | ons     |
| v      | st     | nce     |
| k      | to     | men     |
| x      | nt     | ith     |
| j      | ng     | ted     |
| q      | se     | ers     |
| z      | ha     | pro     |


## Glossary

Several terms and metrics exist to compare keyboard layouts.

### Heatmap

Color-coded map to show where the most frequently typed letters are placed. The most frequent letters are best placed along the homerow and parts of the top row. 

![bold layout heatmap](/assets/layout/heatmap-bold.png)

*heatmap for my layout*


![qwerty layout heatmap](/assets/layout/heatmap-qwerty.png)

*heatmap for QWERTY*

### Finger frequency

The distribution across fingers. Index and middle should be prioritized, followed by ring then pinky.

### Hand balance

The distribution across hands. Ideally 50-50.

### Same-finger bigram

Pressing two keys in succession with the same finger (e.g. ED on qwerty). These are uncomfortable to type and should be minimized. 

Aside from minimizing the SFB%, layouts should also reduce SFB distance. Ideally we want the 2 letters that form a SFB to be on adjacent keys (1U SFB) and we should avoid SFBs that involve having to jump over the home row (2U SFB) like Qwerty CE.


## Trigrams

Trigrams can be categorized in the following ways:


### Alternate

Pressing one key with one hand, then one with the other, then back to the first. e.g. `ala` on QWERTY.


### Roll

pressing two (not same finger) keys with one hand, and a third key with the other. In other words, a 2 key roll following or preceding a hand change.

Rolls are inward or outward depending on the direction the keys typed with the same hand follow. e.g. DF on QWERTY is inward, FD is outward.

Some people prefer inward rolls over outward rolls. The in-roll ratio stat tells us how much a layout favors the former over the latter.

### Onehand

Three keypresses with one hand in the same direction, e.g. SDF on QWERTY

### Redirect

A onehand but the direction changes. e.g. DFS on QWERTY.


## Heuristics

- Consider programming and vim keybindings in corpus
- Fixed zxcv. Handy to have most common shortcuts common when switching to QWERTY
- High hand alternation
- high inward rolls


## Statistics

```json
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


