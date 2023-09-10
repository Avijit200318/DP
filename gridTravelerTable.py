# m = row and n = column. the timecomplexity is O(m*n)
class Solution(object):
    def gridTraveler(self, m, n):
        arr = [[0]*(m+1) for _ in range(n+1)]
        arr[1][1] = 1

        for i in range(m+1):
            for j in range(n+1):
                curr = arr[i][j]
                if j+1 <= n:
                    arr[i][j+1] += curr
                    # we have to run a loop that goes 0 to n so we write range(n+1) and ...
                if i+1 <= m:
                    arr[i+1][j] += curr
        return arr[m][n]
    
s = Solution()
print(s.gridTraveler(3,3))
