class Solution:
    def findDuplicates(self, arr):
        # code here552
        arr.sort()
        ans = []
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                if not ans or ans[-1] != arr[i]:
                    ans.append(arr[i])
        return ans