from typing import List


class Solution:
    """
    1. Problem
        - given a list of tokens representing an arithmetic expression in reverse
          polish notation, evaluate it and return the resulting integer
    2. Plan
        - single stack as accumulator: push numbers, pop two operands on an
          operator and push the result
        - first pop is the RIGHT operand (b), second is the left (a) — matters
          for - and /
        - for division, use int(a / b): float divide then truncate to int, so
          the value moves toward zero (Python // floors toward -inf instead);
          float is exact for LeetCode's 32-bit intermediates
    3. Complexity
        - Time: O(n) | Space: O(n)
    """

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }

        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[token](a, b))

        return stack[-1]
