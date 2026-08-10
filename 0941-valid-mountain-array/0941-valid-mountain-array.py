class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        if len(a)<3:
            return False
        
        if a[0]>a[1]:
            return False

        i=0
        top=0
        while(i<=len(a)-2):
            if(a[i]<a[i+1]):
                i=i+1
            else:
                top=1
                break
        
        while(i<=len(a)-2):
            if(a[i]>a[i+1]):
                i=i+1
            else:
                top=2
                break
        
        if top==1:
            return True
        return False