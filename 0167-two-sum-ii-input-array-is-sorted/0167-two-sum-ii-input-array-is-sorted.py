class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        left=0
        right=len(a)-1
        while left<right:
            total=a[left]+a[right]
            if total==target:
                return[left+1,right+1]
            elif total>target:
                right-=1
            else:
                left+=1