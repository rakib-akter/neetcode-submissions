class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        x = 0
        y = 0
        z = 0

        for num in nums:
            if num == 0:
                x += 1
            elif num == 1:
                y += 1
            else:
                z += 1

        
        index = 0

        for i in range(x):
            nums[index] = 0
            index += 1

        for i in range(y):
            nums[index] = 1
            index += 1

        for i in range(z):
            nums[index] = 2
            index += 1