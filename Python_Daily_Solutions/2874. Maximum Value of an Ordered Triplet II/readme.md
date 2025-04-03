# 2874. Maximum Value of an Ordered Triplet II

## 📌 Problem Statement  
You are given a `0-indexed` integer array `nums`.  
Return the **maximum value** over all ordered triplets `(i, j, k)` such that `i < j < k`. If all such triplets have a negative value, return `0`.  

The value of the triplet `(i, j, k)` is calculated as:  
\[
(nums[i] - nums[j]) \times nums[k]
\]

---

## ✅ Approach & Solution  
Since the constraints are **large (`n ≤ 10^5`)**, a brute-force `O(n³)` solution is infeasible. Instead, we can solve this in **O(n) time** using a greedy approach.  

### **Algorithm**  
1. **Iterate through `nums` while tracking:**  
   - `mx` → Maximum value encountered so far.  
   - `mx_diff` → Maximum difference `(nums[i] - nums[j])` encountered.  
   - `ans` → Maximum valid triplet value.  
2. **Update `ans` at each step** using `mx_diff * nums[k]`.  
3. **Update `mx_diff` and `mx`** accordingly.  
4. **Return `ans`**, ensuring we return `0` if no positive value is found.  

---

## 📌 Code Implementation  
```python
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = mx = mx_diff = 0
        for x in nums:
            ans = max(ans, mx_diff * x)
            mx_diff = max(mx_diff, mx - x)
            mx = max(mx, x)
        return ans
```

---

## 🔥 Complexity Analysis  
- **Time Complexity**: **O(n)** → We traverse `nums` once.  
- **Space Complexity**: **O(1)** → We use only a few integer variables.  

---

## 🛠 Example Walkthrough  

### **Example 1**  
🔹 `nums = [12,6,1,2,7]`  
✔️ Maximum triplet: `(0, 2, 4)`  
✔️ Computation: `(12 - 1) * 7 = 77`  
✅ Output: `77`  

### **Example 2**  
🔹 `nums = [1,10,3,4,19]`  
✔️ Maximum triplet: `(1, 2, 4)`  
✔️ Computation: `(10 - 3) * 19 = 133`  
✅ Output: `133`  

### **Example 3**  
🔹 `nums = [1,2,3]`  
✔️ Only possible triplet: `(0, 1, 2)`  
✔️ Computation: `(1 - 2) * 3 = -3`  
✔️ Since it's negative, return `0`.  
✅ Output: `0`  

---

## 🚀 Alternative Approaches  
1️⃣ **Brute Force (O(n³))**  
   - Check all `(i, j, k)` triplets and compute values.  
   - **Inefficient for `n = 10^5`**.  

2️⃣ **Using Prefix Arrays (O(n²))**  
   - Precompute max values up to `j` and use them for calculations.  

📌 **Why is our approach optimal?**  
🔹 It **avoids unnecessary iterations** and **only keeps track of necessary values**, leading to an efficient **O(n) solution**.  

---

## ❓ Discussion  
💬 **Q: Can this handle large inputs efficiently?**  
✔️ Yes! Our **O(n) solution** works in milliseconds for `n ≤ 10^5`.  

💬 **Q: What if all values in `nums` are the same?**  
✔️ `mx_diff = 0`, so the result will be `0`.  

💬 **Q: Can we solve this using DP?**  
✔️ Yes, but unnecessary since **greedy works optimally in O(n)**.  

💬 **Q: What are some edge cases we should test?**  
✔️ Are there any input cases that might break our approach?  

💬 **Q: Could this be optimized further?**  
✔️ The current solution is already `O(n)`, but is there a way to reduce the number of operations or improve readability?  

---

## 🔥 PRs & Issues Welcome!  
👥 Feel free to suggest optimizations or discuss edge cases! 🚀

