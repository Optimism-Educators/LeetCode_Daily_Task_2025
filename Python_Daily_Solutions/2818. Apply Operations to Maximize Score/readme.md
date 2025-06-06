
# 📄 2818. Apply Operations to Maximize Score  

## 📌 Problem Statement  
You are given an array **`nums`** of **`n`** positive integers and an integer **`k`**.  

### **Operations:**  
You can apply the following **operation at most `k` times**:  
1. **Choose a non-empty subarray** `nums[l, ..., r]` that hasn't been chosen before.  
2. **Pick an element** `x` from the subarray that has the **highest prime score**.  
   - If multiple elements have the same prime score, choose the **one with the smallest index**.  
3. **Multiply your current score by `x`**.  

Your goal is to **maximize the score** after at most `k` operations.  

---

## 🏆 **Prime Score Definition**  
The **prime score** of an integer **`x`** is the **number of distinct prime factors** of `x`.  

**Example Calculation:**  
- **300** → Prime factors: **`2, 3, 5`** → Prime score = **3**  
- **18** → Prime factors: **`2, 3`** → Prime score = **2**  
- **19** → Prime factors: **`19`** → Prime score = **1**  

Since the answer may be **large**, return it **modulo `10⁹ + 7`**.

---

## 🗂 **Constraints**  
- **`1 ≤ nums.length == n ≤ 10⁵`**  
- **`1 ≤ nums[i] ≤ 10⁵`**  
- **`1 ≤ k ≤ min(n * (n + 1) / 2, 10⁹)`**  

---

## 🔢 **Example 1**  

### **Input:**  
```python
nums = [8,3,9,3,8] 
k = 2
```
### **Output:**  
```python
81
```
### **Explanation:**  
To maximize the score:  
1️⃣ **Choose subarray `nums[2, ..., 2]`**  
   - `nums[2] = 9` (Prime score = **1**)  
   - Multiply score: `1 * 9 = 9`  

2️⃣ **Choose subarray `nums[2, ..., 3]`**  
   - `nums[2] = 9` again (highest prime score, smallest index)  
   - Multiply score: `9 * 9 = 81`  

✅ **Final Score = `81`**  

---

## 🔢 **Example 2**  

### **Input:**  
```python
nums = [19,12,14,6,10,18] 
k = 3
```
### **Output:**  
```python
4788
```
### **Explanation:**  
To maximize the score:  
1️⃣ **Choose subarray `nums[0, ..., 0]`**  
   - `nums[0] = 19` (Prime score = **1**)  
   - Multiply score: `1 * 19 = 19`  

2️⃣ **Choose subarray `nums[5, ..., 5]`**  
   - `nums[5] = 18` (Prime score = **2**)  
   - Multiply score: `19 * 18 = 342`  

3️⃣ **Choose subarray `nums[2, ..., 3]`**  
   - `nums[2] = 14` (Prime score = **2**, smaller index)  
   - Multiply score: `342 * 14 = 4788`  

✅ **Final Score = `4788`**  

---

## 🚀 **Optimized Approach**  

### **Steps to Solve:**  
1️⃣ **Precompute the Prime Score** for numbers **`1 ≤ x ≤ 10⁵`** using a **modified Sieve of Eratosthenes**.  
2️⃣ **Generate all subarray elements (`n * (n+1) / 2`)** and store their `(prime_score, value, index)`.  
3️⃣ **Sort the elements** by **highest prime score** (descending) and **smallest index**.  
4️⃣ **Select `k` highest elements** to maximize the score.  

---

## 🐍 **Python Solution**  

```python
import math
from heapq import nlargest
from collections import defaultdict

MOD = 10**9 + 7

def count_prime_factors(n):
    """Returns the number of distinct prime factors of n."""
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return len(factors)

def precompute_prime_scores(limit=10**5):
    """Precomputes the prime scores for numbers from 1 to limit."""
    prime_scores = [0] * (limit + 1)
    
    for i in range(2, limit + 1):
        if prime_scores[i] == 0:  # `i` is a prime
            for j in range(i, limit + 1, i):
                prime_scores[j] += 1  # Mark multiples of `i`
    
    return prime_scores

def maxScore(nums, k):
    """Computes the maximum score using `k` operations."""
    prime_scores = precompute_prime_scores(max(nums))

    # Store elements as (prime_score, value, index)
    elements = []
    
    for i, num in enumerate(nums):
        elements.append((prime_scores[num], num, i))
    
    # Sort by (prime_score descending, value descending, index ascending)
    elements.sort(reverse=True, key=lambda x: (x[0], x[1], -x[2]))

    # Take `k` highest scoring elements
    result = 1
    for _, value, _ in elements[:k]:
        result = (result * value) % MOD

    return result
```

---

## 💡 **Time Complexity Analysis**  
- **Precompute Prime Scores:** **`O(N log log N)`** (Sieve)  
- **Extract Elements:** **`O(N)`**  
- **Sort Elements:** **`O(N log N)`**  
- **Select `k` elements:** **`O(K log K)`**  

✅ **Overall Complexity:** **`O(N log N) + O(K log K)`** (Efficient for `N ≤ 10⁵`)  

---

## 📂 **File Structure**  
```
LeetCode-Daily-Task/
│── 📁 problems/
│   ├── 2818_maximize_score.py
│   ├── 2736_sliding_window.py
│── 📁 datasets/  
│   ├── prime_scores.csv
│── README.md  
│── requirements.txt  
```

---

## 🔥 **Want to Participate?**  
🚀 Solve more **LeetCode Hard problems** in **Python**!  

| #    | Problem Name                           | Solution                                  | LeetCode Link                                                                   |
| ---- | -------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------- |
| 2818 | **Apply Operations to Maximize Score** | [🔗 View](problems/2818_maximize_score.py) | [🔗 LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-score/) |
| 2736 | **Sliding Window Maximum**             | [🔗 View](problems/2736_sliding_window.py) | [🔗 LeetCode](https://leetcode.com/problems/sliding-window-maximum/)             |

---

## 🔗 **Useful Links**  
- 📘 [LeetCode Hard Problems](https://leetcode.com/problemset/all/?difficulty=Hard)  
- 🐍 [Python Prime Factorization](https://docs.python.org/3/library/math.html#math.factorial)  
- 🌟 [Contribute on GitHub](https://github.com/your-username/LeetCode_Hard_Problems)  

---

💡 **Let's learn, code, and master hard problems together! 🚀**

