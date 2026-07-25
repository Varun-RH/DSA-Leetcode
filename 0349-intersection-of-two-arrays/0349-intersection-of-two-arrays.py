class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        ans=[]
        for num in set(nums2):
            if num in s1:
                ans.append(num)
        return ans