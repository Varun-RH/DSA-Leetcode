class Solution:
    def checkIfExist(self, a: List[int]) -> bool:
        for i in range(0,len(a)-1+1,1):
            for j in range(0,len(a)-1+1,1):
                if(a[i]==2*a[j] and i!=j):
                    return True
        
        return False