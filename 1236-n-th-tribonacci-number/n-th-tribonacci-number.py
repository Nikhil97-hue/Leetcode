class Solution:
    def tribonacci(self, n: int) -> int:
        fib1=0
        fib2=1
        fib3=1
        i=3
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1

        while i<=n:
            sum=fib1+fib2+fib3
            fib1=fib2
            fib2=fib3
            fib3=sum
            i+=1
        return sum
        