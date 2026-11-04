class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem: Find the longest substring with no repeated characters.
        Edge cases: Empty input and duplicates at either window edge.
        Plan: Shrink from the left until the right character is unique.
        Complexity: O(n) time and O(min(n, |Σ|)) space.
        Variant: Checking every substring takes O(n^2) time.
        """
        window = set()
        left = 0
        right = 0
        best = 0

        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
                best = max(best, len(window))
                right += 1

        return best


if __name__ == "__main__":
    solution = Solution()
    for text, expected in (
        ("", 0),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("au", 2),
    ):
        assert solution.lengthOfLongestSubstring(text) == expected, text
