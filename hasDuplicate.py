class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        sorted_nums = sorted(nums, reverse=True)

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True

        return False

    def hasDuplicate2(self, nums: list[int]) -> bool:
        numsSet = set(nums)

        if len(nums) > len(numsSet):
            return True

        return False

    def hasDuplicate3(self, nums: list[int]) -> bool:
        hashSet: set[int] = set()

        for n in nums:
            if n in hashSet:
                return True

            hashSet.add(n)

        return False


solution = Solution()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(solution.hasDuplicate(nums))
print(solution.hasDuplicate2(nums))
print(solution.hasDuplicate3(nums))
