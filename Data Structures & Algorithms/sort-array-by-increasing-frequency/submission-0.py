class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        def sort_rule(x):
            return (count[x], -x)
        
        return sorted(nums, key= sort_rule)
        
        