# the time complexity of this code is O(n^m * m)
# class Solution(object):
#     def countCreate(self, target, wordBank):
#         if target == '':
#             return 1
        
#         res = 0

#         for word in wordBank:
#             if target.startswith(word):
#                 suffix = target[len(word):]
#                 noWay = self.countCreate(suffix, wordBank)
#                 res += noWay
#         return res
    
class Solution(object):
    def countCreate(self, target, wordBank, memo={}):
        if target in memo:
            return memo[target]
        if target == '':
            return 1
        
        count = 0

        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                noWay = self.countCreate(suffix, wordBank)
                count += noWay
        return count
        

s = Solution()
print(s.countCreate("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(s.countCreate("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))

#the timecomplexity is O(n*m^2)
