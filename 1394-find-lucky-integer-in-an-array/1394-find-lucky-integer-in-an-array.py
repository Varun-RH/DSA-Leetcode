class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        max_num=-1
        for num in freq:
            if num==freq[num]:
                max_num=max(max_num,num)
        return max_num