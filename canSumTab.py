class Solution(object):
    def canSum(self, target, numbers):
        arr = [False]*(target*2)
        # for javascript the above line should be (target+1).but since python array work different unlike javascript thats why we need to increase the size so the loop did not goes out of index.
        #we can use (target+1+max(numbers)) but it give us an extra time complexity O(n).
        #thats why we use target*2 here.
        arr[False] = True

        for i in range(target + 1):
            if  arr[i] == True:
                for num in numbers:
                    arr[i+num] = True

        return arr[target]

s = Solution()
print(s.canSum(7,[2,3]))
print(s.canSum(8,[2,3,5]))
print(s.canSum(300,[7,14]))
