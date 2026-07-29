class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=1
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in freq:
                ans.append(i)
        return ans
        