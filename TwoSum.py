# Two Sum leetcode problem
class Solution:
    def twoSum(self, arr, x):
        ans = [0, 0]
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == x:
                    ans[0] = i
                    ans[1] = j
        
        return ans
arr = list(map(int, input("Enter array: ").split()))
x = int(input("Enter target: "))

obj = Solution()
result = obj.twoSum(arr, x)

print("Indices:", result)