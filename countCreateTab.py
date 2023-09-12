class Solution(object):
    def countConstruct(self, target, wordBank):
        arr = [0]*(len(target)*2)
        arr[0] = 1

        for i in range(len(target)+1):
            if arr[i] != 0:
                for word in wordBank:
                    if target[i: i+len(word)] == word:
                        arr[i + len(word)] += arr[i]
        return arr[len(target)]

s = Solution()
print(s.countConstruct("purple", ['purp','p','ur','le','purpl']))
print(s.countConstruct("abcdef", ['ab','abc','cd','def','abcd']))
print(s.countConstruct("purple", ['p','ur','l','erpl']))
