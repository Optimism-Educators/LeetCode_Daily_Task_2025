

# 2140. Solving Questions With Brainpower

## 📌 Problem Statement
You are given a 0-indexed 2D integer array `questions` where `questions[i] = [pointsi, brainpoweri]`.  
For each question, you must decide whether to **solve** it or **skip** it:
- **Solve:** Earn `pointsi` points, but you must skip the next `brainpoweri` questions.
- **Skip:** Move to the next question without earning any points.

The goal is to maximize the total points earned by processing the questions in order.

---

## 📊 Table Structure

Although this problem is algorithmic in nature and doesn't use a database, we can imagine a **Questions Table** that represents each question. For demonstration purposes, we’ll show a sample table structure similar to a "Teacher Table":

### Teacher Table (Questions Table)
| QuestionID | Points | Brainpower |
| ---------- | ------ | ---------- |
| 0          | 3      | 2          |
| 1          | 4      | 3          |
| 2          | 4      | 4          |
| 3          | 2      | 5          |

---

## 📊 Example 1

### Input: Teacher Table
| QuestionID | Points | Brainpower |
| ---------- | ------ | ---------- |
| 0          | 3      | 2          |
| 1          | 4      | 3          |
| 2          | 4      | 4          |
| 3          | 2      | 5          |

### Output:
```
5
```

### Explanation:
- **Solve question 0:** Earn 3 points, then skip questions 1 and 2.
- **Solve question 3:** Earn 2 points.
- **Total points:** 3 + 2 = 5.


---

## ✅ Approach: Python (Recursion with Memoization)
We use a recursive depth-first search (DFS) with memoization to decide for each question whether to solve it or skip it.  
For each question `i`:
- **Solve:** Add `pointsi` and then jump to question `i + brainpoweri + 1`.
- **Skip:** Move to question `i + 1`.

The recurrence is:
```python
dfs(i) = max(pointsi + dfs(i + brainpoweri + 1), dfs(i + 1))
```

---

## 🐍 Python (Pandas) Solution 1

```python
from functools import cache
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            p, b = questions[i]
            return max(p + dfs(i + b + 1), dfs(i + 1))
        
        return dfs(0)
```

## 🐍 Python (Pandas) Solution 2

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            p, b = questions[i]
            return max(p + dfs(i + b + 1), dfs(i + 1))

        return dfs(0)
```

### ✅ Approach Explanation:
- **Recursion with Memoization:** The function `dfs(i)` computes the maximum points achievable starting from the `i`th question.
- **Decision:** For each question, it chooses the maximum between solving the question (adding its points and skipping the next `brainpower` questions) and skipping the question.
- **Efficiency:** The use of caching (`@cache`) ensures each state is computed only once.

---

## 📁 File Structure

```plaintext
.
├── README.md          # This file
└── solution.py        # Contains the Python solution implementation
```

---

## 🔗 Useful Links
- [LeetCode Problem 2140](https://leetcode.com/problems/solving-questions-with-brainpower/)
- [Dynamic Programming - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Python functools.cache Documentation](https://docs.python.org/3/library/functools.html#functools.cache)
