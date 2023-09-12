# the time complexity of this code is O(m^2*n)
class Solution(object):
    def canConstract(self, target, wordBank):
        arr = [False]*(len(target)*2)
        arr[0] = True

        for i in range(len(target)+1):
            if arr[i] == True:
                for word in wordBank:
                    if target[i: i+len(word)] == word:
                        arr[i+len(word)] = True
        return arr[len(target)]
    
s = Solution()
print(s.canConstract("abcdef", ['ab','abc','cd','def','abcd']))
print(s.canConstract("skateboard", ['bo','rd','at','t','ska','sk']))
print(s.canConstract("eeeeeeeeeeeeeef", ['e','ee','eee','eeee','eeeee','eeeeee','eeeeeeee']))
