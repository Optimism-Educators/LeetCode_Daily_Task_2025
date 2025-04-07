# Partition Equal Subset Sum

## Problem Statement
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, otherwise return `false`.

## Examples

### Example 1:
**Input:**
```plaintext
nums = [1,5,11,5]
```
**Output:**
```plaintext
true
```
**Explanation:**
The array can be partitioned as `[1, 5, 5]` and `[11]`.

### Example 2:
**Input:**
```plaintext
nums = [1,2,3,5]
```
**Output:**
```plaintext
false
```
**Explanation:**
The array cannot be partitioned into equal sum subsets.

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Approach
The problem can be solved using **Dynamic Programming (Subset Sum Problem)**:
1. Compute the total sum of the array.
2. If the total sum is odd, return `false` (since it's impossible to split into two equal parts).
3. Use a **0/1 Knapsack** approach to determine if a subset with sum `total_sum/2` exists.
4. Use a **bottom-up DP approach** to check if we can form the required sum.

## Solution
The solution uses a **boolean DP array** `dp[i]`, where `dp[i]` is `true` if a subset with sum `i` can be formed.
- Initialize `dp[0] = true` (sum `0` is always possible).
- Iterate over each number in `nums`, updating the `dp` array in reverse order.
- If `dp[target]` is `true`, return `true`, otherwise return `false`.
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m, mod = divmod(sum(nums), 2)
        if mod:
            return False
        n = len(nums)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(nums, 1):
            for j in range(m + 1):
                f[i][j] = f[i - 1][j] or (j >= x and f[i - 1][j - x])
        return f[n][m]
```

## Complexity Analysis
- **Time Complexity:** `O(n * sum/2)`, where `n` is the number of elements.
- **Space Complexity:** `O(sum/2)`, optimized using a 1D DP array.

## Usage
To run the solution, use the following function:
```python
from solution import canPartition
print(canPartition([1,5,11,5]))  # Output: True
print(canPartition([1,2,3,5]))   # Output: False
```

