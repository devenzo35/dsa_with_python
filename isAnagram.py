class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_str1 = sorted(s)
        sorted_str2 = sorted(t)

        if sorted_str1 == sorted_str2:
            return True

        return False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS: dict[str, int] = {}
        countT: dict[str, int] = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in countS:
            if countS[c] != countT.get(c):
                return False

        return True


anagram = Solution()

solution = anagram.isAnagram(s="jar", t="jam")
solution2 = anagram.isAnagram2(s="racecar", t="carrace")

print(solution2)
