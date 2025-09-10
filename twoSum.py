class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap: dict[int, int] = {}

        for idx, num in enumerate(nums):
            t = target - num

            if t in hashMap:
                return [hashMap[t], idx]

            hashMap[num] = idx

        return []


exercise = Solution()
solution1 = exercise.twoSum(nums=[1, 3, 4, 2], target=6)
