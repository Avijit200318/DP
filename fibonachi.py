#normal solution time complexity O(2^n)
# class Solution(object):
#     def fib(self, n):
#         if n == 0: return 0
#         if n <= 2: return 1
#         return self.fib(n-1) + self.fib(n-2)

# s = Solution()
# print(s.fib(5))

'''fibonachi using dynamic programming . using memo. whose time complexity O(n)'''
class Solution(object):
    def fib(self, n):
        memo = {}
        if n in memo: return memo[n]
        if n == 0: return 0
        if n <= 2: return 1
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
    
s = Solution()
print(s.fib(28))