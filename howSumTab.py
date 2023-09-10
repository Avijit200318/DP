# the time complexity of this code is O(n*m^2).we use table method.one of the DP method.

class Solution(object):
    def howSum(self, target, numbers):
        arr = [None]*(target*2)
        arr[0] = []

        for i in range(target+1):
            if arr[i] != None:
                for num in numbers:
                    arr[i+num] = [*arr[i],num]
        return arr[target]
        
    
s = Solution()
print(s.howSum(8,[2,3,5]))
print(s.howSum(300, [7,14]))