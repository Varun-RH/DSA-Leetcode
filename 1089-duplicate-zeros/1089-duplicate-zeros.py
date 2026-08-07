class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        ans=[]
        for i in arr:
            if i!=0:
                ans.append(i)
            else:
                ans.append(0)
                ans.append(0)
        x=0
        for i in range(0,len(arr)-1+1,1):
            arr[i]=ans[x]
            x=x+1