class Solution(object):
    def allConstruct(self, target, wordBank, memo={}):
        if target in memo:
            return memo[target]
        if target == '':
            return [[]]
        
        result = []

        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                suffixWays = self.allConstruct(suffix, wordBank, memo)
                for way in suffixWays:
                    result.append([word] + way)

        memo[target] = result
        return result

s = Solution()
print(s.allConstruct('purple', ['pur', 'p', 'ur', 'le', 'purpl']))
print(s.allConstruct('abcdef', ['ab', 'abc','cd','def','abcd','ef','c']))
