def minOperationsToDistinct(nums):
    seen = set()
    count = 0
    while len(set(nums)) != len(nums):
        nums = nums[3:]  # Remove first 3 elements
        count += 1
    return count