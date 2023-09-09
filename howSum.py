# if there is any posible solution then return any one of then. the normal code time complexity is O(n*m^2)

# class Solution(object):
#     def howSum(self, target, numbers):
#         if target == 0:
#             return []
#         if target < 0:
#             return None
        
#         for num in numbers:
#             rem = target - num
#             reCom = self.howSum(rem, numbers)
#             if reCom != None:
#                 return [*reCom, num]
#         return None
    
class Solution(object):
    def howSum(self, target, numbers, memo={}):
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        if target < 0:
            return None
        
        for num in numbers:
            rem = target - num
            reCom = self.howSum(rem, numbers, memo)
            if reCom != None:
                memo[target] = [*reCom, num]
                return memo[target]
        memo[target] = None
        return None
        

s = Solution()
print(s.howSum(7, [2,3]))
print(s.howSum(300, [7, 14]))

# the time complexity become O(n*m^2)
