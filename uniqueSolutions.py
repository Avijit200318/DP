#unique paths or grid problem. time complexity O(2^(m+n)) .the time complexity is very high so it did not work for large value.

# class Solution(object):
#     def uniquePath(self, m, n):
#         if m == 1 and n == 1: return 1
#         if m == 0 or n == 0: return 0
#         return self.uniquePath(m - 1, n) + self.uniquePath(m, n - 1)

#using dynamic programming . time complexity: O(m*n)

class Solution(object):
    def uniquePath(self, m, n):
        memo = {}
        def helper(m, n):
            if (m,n) in memo: return memo[(m,n)]
            if m == 1 and n == 1: return 1
            if m == 0 or n == 0: return 0
            memo[(m,n)] = helper(m -1 , n) + helper(m, n-1)
            return memo[(m,n)]
        return helper(m,n)

s = Solution()
print(s.uniquePath(3, 7))