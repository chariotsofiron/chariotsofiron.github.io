+++
title = "Proofs"
slug = "proofs"
date = 2023-02-01
+++

# Infinitely many primes

(by reductio ad absurdum)

Suppose there were finitely many primes: $p_1, p_2, ..., p_n$.

Let $Q = p_1 \cdot p_2 \cdot ... \cdot p_n + 1$

By construction, $Q$ is not divisible by any $p_i$.

Hence $Q$ is either prime itself, or divisible by another prime greater than $p_n$


# Square root of 2 is irrational

(by contradiction)

1. Suppose $\sqrt{2}$ was rational. Then $\sqrt{2} = \frac{p}{q}$ where $p,q$ share no common factors
2. Squaring both sides $2 = \frac{p^2}{q^2}$ and rearranging $2q^2 = p^2$
3. Hence $p^2$ is even and thus so is $p$ i.e. $p = 2k$
4. Substituting into (2) $2q^2 = (2k)^2 = 4k^2$ => $q^2 = 2k^2$
5. So $q$ is also even, but $p,q$ share no common factors
6. Our supposition is wrong so $\sqrt{2}$ is not rational


# Halting problem

Halting problem: Given a program $P$ and an input string $I$, output $1$ if $P$ halts on $I$ and $0$ if $P$ goes into an infinite loop.

(by contradiction)

Suppose there exists a program $\text{halt}(P, I)$ that solves the halting problem. Then we could write a program $z$

```
fn z(string x):
    if halt(x, x):
        loop forever
    else:
        halt
```

Suppose we feed program $z$ into itself, there are two cases
1. if `z(z)` halts => `halt(z, z) = true` => program z loops forever. Contradiction.
2. if `z(z)` loops forever => `halt(z, z) = false` => program Z halts. Contradiction.


# Real numbers are uncountable


# Irrational number to the power of another can be rational

