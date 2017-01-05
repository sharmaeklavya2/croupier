# Guessing game

In this game, the computer will choose a number `k` from 1 to `n` and you have to guess it.
`n` can range from 1 to 10<sup>9</sup>.

First you have to take `n` as input from the computer.

You can then query the computer in this format: `? a b`. Here `a` and `b` are numbers.
The computer can have 2 possible responses: `in` and `out`.
It will say `in` if `k` is in the range `a` to `b` or `b` to `a` (both inclusive) and `out` otherwise.

If you have determined what `k` is, output `! k`.

If you have made `q` queries, your score will be `(log2(n) + 1) / (q + 1)` (`log2` means base 2 logarithm).

### Sample interaction

Assume computer chose `n` as 20 and `k` as 10.

```
computer: 20
player: ? 1 10
computer: in
player: ? 1 5
computer: out
player: ? 6 8
computer: out
player: ? 9 9
computer: out
player: ! 10
```

This gives a correct answer in 4 queries with a score of 1.06438561898.
