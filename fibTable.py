# the time complexity of this code is O(n).we use table method.one of the DP method.

class Solution(object):
    def fib(self, n):
        arr = [0]*(n+3)
        # if we use javaScript then the array is work different unlike other language array. so for python we need a array that has extra 2 space.since the fib(n) = fib(n-1)+fib(n-2).
        arr[1] = 1
        # this is the base case for the fibonachi series.
        for i in range(n+1):
            if(i+2 <= n+1):
                arr[i+2] += arr[i]
                arr[i+1] += arr[i]
        return arr[n]
    
s = Solution()
print(s.fib(50))