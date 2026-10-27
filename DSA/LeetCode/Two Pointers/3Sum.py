class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Problem: return all triplets nums[i], nums[j], and nums[k] ensuring that indices are not repeated e.g. [j,j,k], [i,i,j], etc
        Edge Cases: all positive, all negative, all zeroes
        Plan: Two pointer approach adjusting left and right pointers while having an anchor i for each iteration
        Complexity: O(n^2)
        Variant: Brute force O(n^3)
        """
        ans = []
        n = len(nums)

        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l_val = nums[l]
                    r_val = nums[r]

                    ans.append([nums[i], l_val, r_val])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == l_val:
                        l += 1

                    while l < r and nums[r] == r_val:
                        r -= 1

        return ans
