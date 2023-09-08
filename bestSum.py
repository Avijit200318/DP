# normal method in this case the time complexity is O(n*m^2) . n = [length of the array] and m = [targetSum or in this case target].

# class Solution(object):
#     def bestSum(self, target, numbers):
#         if target == 0: return []
#         if target < 0 : return None;

#         shortCombination = None

#         for num in numbers:
#             rem = target - num
#             reComb = self.bestSum(rem, numbers);
#             if reComb != None:
#                 combination = [*reComb, num]
#                 if shortCombination == None or len(shortCombination) > len(combination):
#                     shortCombination = combination
#         return shortCombination
    
class Solution(object):
    def bestSum(self, target, numbers, memo={}):
        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0 : return None;

        shortCombination = None

        for num in numbers:
            rem = target - num
            reComb = self.bestSum(rem, numbers, memo);
            if reComb != None:
                combination = [*reComb, num]
                if shortCombination == None or len(shortCombination) > len(combination):
                    shortCombination = combination
        memo[target] = shortCombination
        return shortCombination
    
s = Solution()
print(s.bestSum(7, [5,3, 4, 7]))
print(s.bestSum(8, [2, 3, 5]))
print(s.bestSum(8,[1, 4, 5]))
print(s.bestSum(100, [1,2, 5,25]))

# the time complexity of this code is O(n*m^2). just using the memo.
