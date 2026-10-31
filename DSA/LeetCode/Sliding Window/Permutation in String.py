from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Problem: Check whether s2 contains a permutation of s1.
        Edge cases: s1 is longer than s2; match in first or last window; repeats.
        Plan: Count s1 and the first window, then slide by one character at a time.
        Complexity: O(n) time and O(1) space for lowercase English letters.
        Variant: Recounting each window takes O(n * m) time.
        """
        window_size = len(s1)
        if window_size > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:window_size])
        if target == window:
            return True

        for right in range(window_size, len(s2)):
            outgoing = s2[right - window_size]
            window[outgoing] -= 1
            if window[outgoing] == 0:
                del window[outgoing]

            window[s2[right]] += 1
            if window == target:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    for s1, s2, expected in (
        ("ab", "ab", True),
        ("ab", "eidba", True),
        ("aab", "eidbaaoo", True),
        ("ab", "eidboaoo", False),
        ("abc", "ab", False),
    ):
        assert solution.checkInclusion(s1, s2) is expected, (s1, s2)
