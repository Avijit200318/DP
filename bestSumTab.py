# the time complexity of this code is O(n*m^2).we use table method.one of the DP method.

class Solution(object):
    def bestSum(self, target, numbers):
        arr = [None]*(target*3)
        # in this case index is out of range. so to use the table method the javascript is more suitable.
        arr[0] = []

        for i in range(target+1):
            if arr[i] != None:
                for num in numbers:
                    combination = [*arr[i], num]
                    if arr[i+num] == None or len(arr[i+num]) > len(combination):
                        arr[i+num] = combination
        return arr[target]
        
    
s = Solution()
print(s.bestSum(8,[2,3,5]))
print(s.bestSum(100, [1,2,5,25]))
print(s.bestSum(7,[5,3,4,7])) #this line goes out of index if we do target*2.