#canSum(target, arry) print true if we made the target and false if not
#normal solution. timecomplexity O(m ^ n). [m = target and n = length of the array]

# class Solution(object):
#     def canSum(self, target, numbers):
#         if target == 0: return 1
#         if target < 0: return 0
#         for num in numbers:
#             rem = target - num
#             if(self.canSum(rem, numbers) == True):
#                 return True
#         return False

class Solution(object):
    def canSum(self, target, numbers):
        memo = {}
        if target in memo: return memo[target]
        if target == 0: return 1
        if target < 0: return 0
        for num in numbers:
            rem = target - num
            if(self.canSum(rem, numbers) == True):
                memo[target] = True
                return True
        memo[target] = False
        return False
    

s = Solution()
print(s.canSum(7, [2,3]))
print(s.canSum(300, [7,4]))