class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the value and its corresponding index
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement already exists in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index
            
        return []