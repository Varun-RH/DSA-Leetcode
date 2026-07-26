class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=n
        digit_sum=0
        digit_product=1
        while n!=0:
            r=n%10
            digit_sum+=r
            digit_product*=r
            n//=10
        total=digit_sum+digit_product
        if x%total==0:
            return True
        else:
            return False
