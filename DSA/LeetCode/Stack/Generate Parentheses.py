class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Problem: Generate all combinations of n pairs of valid parentheses.
        Edge cases: n = 1; n = 2 covers nested and separate pairs.
        Plan: Backtrack over valid prefixes: open if opened < n, and close
            only if closed < opened. Undo each choice after exploring it.
        Complexity: O(n * C_n) time, where C_n is the nth Catalan number;
            O(n) auxiliary space, excluding the O(n * C_n) output.
        Variant: Generate all 4^n strings and validate each in O(n * 4^n) time.
        """
        ans = []
        path = []

        def explore(opened, closed):
            if opened == n and closed == n:
                ans.append("".join(path))
                return

            if opened < n:
                path.append("(")
                explore(opened + 1, closed)
                path.pop()

            if closed < opened:
                path.append(")")
                explore(opened, closed + 1)
                path.pop()

        explore(0, 0)
        return ans


if __name__ == "__main__":
    solution = Solution()
    for pairs, expected in (
        (1, {"()"}),
        (2, {"(())", "()()"}),
        (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
    ):
        results = solution.generateParenthesis(pairs)
        assert set(results) == expected, results
        assert len(results) == len(expected), results
