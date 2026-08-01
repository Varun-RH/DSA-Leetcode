class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h=set(nums)
        i=1
        while True:
            if i not in h:
                return i
            i+=1
            