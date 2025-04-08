# 📄 3396. Minimum Number of Operations to Make Elements in Array Distinct  

## 📌 Problem Statement  
You are given an integer array **`nums`**. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:

### **Operations:**  
1. **Remove the first 3 elements** from the array. If the array has fewer than 3 elements, remove all remaining elements.
2. Repeat this process until all elements in the array are distinct.
3. The goal is to **find the minimum number of operations** needed.

---

## 🗂 **Constraints**  
- **`1 ≤ nums.length ≤ 100`**  
- **`1 ≤ nums[i] ≤ 100`**  

---

## 🔢 **Example 1**  

### **Input:**  
```python
nums = [1,2,3,4,2,3,3,5,7]
```
### **Output:**  
```python
2
```
### **Explanation:**  
1️⃣ **Remove first 3 elements:** `[4, 2, 3, 3, 5, 7]`  
2️⃣ **Remove next 3 elements:** `[3, 5, 7]` (distinct now)  
✅ **Answer = `2`**

---

## 🔢 **Example 2**  

### **Input:**  
```python
nums = [4,5,6,4,4]
```
### **Output:**  
```python
2
```
### **Explanation:**  
1️⃣ **Remove first 3 elements:** `[4, 4]`  
2️⃣ **Remove remaining elements:** `[]` (distinct now)  
✅ **Answer = `2`**

---

## 🔢 **Example 3**  

### **Input:**  
```python
nums = [6,7,8,9]
```
### **Output:**  
```python
0
```
### **Explanation:**  
The array is already distinct. ✅

---

## 🚀 **Optimized Approach**  

### **Steps to Solve:**  
1️⃣ **Count duplicate elements** in the array.  
2️⃣ **Calculate the number of removals required** to eliminate duplicates.
3️⃣ **Perform removal in groups of 3** to reach a distinct set efficiently.  

---

## 🐍 **Python Solution**  

```python
def minOperationsToDistinct(nums):
    seen = set()
    count = 0
    while len(set(nums)) != len(nums):
        nums = nums[3:]  # Remove first 3 elements
        count += 1
    return count

# Example Usage
nums = [1,2,3,4,2,3,3,5,7]
print(minOperationsToDistinct(nums))  # Output: 2
```

---

## 💡 **Time Complexity Analysis**  
- **Checking for duplicates:** **`O(N)`**  
- **Removing elements:** **`O(N)`** (max 34 operations for `N=100`)  

✅ **Overall Complexity:** **`O(N)`** (Efficient for `N ≤ 100`)  

---

## 📂 **File Structure**  
```
MinOps-DistinctArray/
│── 📁 problems/
│   ├── 3396_min_operations.py
│── README.md  
│── requirements.txt  
```

---

## 🔥 **Want to Participate?**  
🚀 Solve more **LeetCode Easy problems** in **Python**!  

| #    | Problem Name                              | Solution                                  | LeetCode Link                                                                                                |
| ---- | ----------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 3396 | **Min Operations to Make Array Distinct** | [🔗 View](problems/3396_min_operations.py) | [🔗 LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/) |

---

## 🔗 **Useful Links**  
- 📘 [LeetCode Easy Problems](https://leetcode.com/problemset/all/?difficulty=Easy)  
- 🐍 [Python Set Operations](https://docs.python.org/3/library/stdtypes.html#set)  
- 🌟 [Contribute on GitHub](https://github.com/your-username/LeetCode_Easy_Problems)  

---

💡 **Let's learn, code, and master easy problems together! 🚀**
