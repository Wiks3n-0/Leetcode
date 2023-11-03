class Solution(object):
    def moveZeroes(self, nums):
        zeroes_count = nums.count(0)
        
        for i in range(zeroes_count):
            nums.remove(0)
        for i in range(zeroes_count):
            nums.append(0)
        print(nums)
x = Solution()

print(x.moveZeroes([1,2,0,0,2,3,0,0]))
        
        