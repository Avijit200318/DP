# in this code the time complexity is O(n^m * m) m = length of the target, n = length of the wordBank
# class Solution(object):
#     def canCreate(self, target, wordBank):
#         if target == '':
#             return True
        
#         for word in wordBank:
#             if target.startswith(word):
#                 suffix = target[len(word):]
#                 if(self.canCreate(suffix, wordBank) == True):
#                     return True
#         return False
    
class Solution(object):
    def canCreate(self, target, wordBank, memo={}):
        if target in memo:
            return memo[target]
        if target == '':
            return True
        
        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                if(self.canCreate(suffix, wordBank, memo)):
                    return True
        return False


s = Solution()
print(s.canCreate("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))

# now in this updated code the time complexity is O(n*m^2)