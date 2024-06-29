+++
title = "Demo page"
+++

A table

| a   | b   | c   |
| --- | --- | --- |
| 1   | 2   | 3   |

Some rust code

```rust
for i in 0..10 {
    println!("{i}");
}
```

Some python code

```python
for i in range(10):
    print(i)
```

Some inline math $1+2$

$$2+x$$

An image

![A picture](image.webp)

> A quote

Some commentary.

## Theorem

There exist irrational numbers $a$ and $b$ such that $a^b$ is rational.

## Proof

We will prove this by constructing a specific example.

1. Let $a = \sqrt{2}$. We know $\sqrt{2}$ is irrational.

1. Consider $(\sqrt{2})^{\sqrt{2}}$. We have two possibilities:

   a) If $(\sqrt{2})^{\sqrt{2}}$ is rational, we've found our example and the proof is complete.

   b) If $(\sqrt{2})^{\sqrt{2}}$ is irrational, we proceed to the next step.

1. Assume $(\sqrt{2})^{\sqrt{2}}$ is irrational. Let's call this number $x$:

   $x = (\sqrt{2})^{\sqrt{2}}$

1. Now consider $x^{\sqrt{2}}$. We can rewrite this as:

   $x^{\sqrt{2}} = ((\sqrt{2})^{\sqrt{2}})^{\sqrt{2}}$

1. Using the laws of exponents, we can simplify:

   $((\sqrt{2})^{\sqrt{2}})^{\sqrt{2}} = (\sqrt{2})^{\sqrt{2} \cdot \sqrt{2}} = (\sqrt{2})^2 = 2$

1. 2 is clearly rational.

Therefore, we have shown that $x^{\sqrt{2}} = 2$, where $x$ is irrational (by our assumption in step 3) and $\sqrt{2}$ is irrational.

## Conclusion

We have constructed irrational numbers $a$ and $b$ (namely, $x$ and $\sqrt{2}$) such that $a^b$ is rational (specifically, equal to 2).

This proves that it's possible for an irrational number raised to an irrational power to be rational.

Q.E.D.
