---

# **2503. Maximum Number of Points From Grid Queries**  

## **Problem Statement**  
You are given an `m x n` integer matrix `grid` and an array `queries` of size `k`.  

Find an array `answer` of size `k` such that for each integer `queries[i]`, you start in the **top-left cell** of the matrix and repeat the following process:  

1. If `queries[i]` is **strictly greater** than the value of the current cell, then:  
   - You **gain one point** if it is your **first time** visiting this cell.  
   - You can **move** to any adjacent cell **(up, down, left, or right)**.  
2. Otherwise, you **stop the process** and gain no more points.  

After processing each query, `answer[i]` is the **maximum number of points** you can collect.  
- **You can visit the same cell multiple times** for different queries.  

Return the resulting array `answer`.  

---

## **Example 1**  

### **Input:**  
```plaintext
grid = [[1,2,3],
        [2,5,7],
        [3,5,1]]
queries = [5,6,2]
```

### **Output:**  
```plaintext
[5,8,1]
```

### **Explanation:**  
For each query:  
- **Query = 5**: Visit `5` cells.  
- **Query = 6**: Visit `8` cells.  
- **Query = 2**: Visit `1` cell.  

---

## **Example 2**  

### **Input:**  
```plaintext
grid = [[5,2,1],
        [1,1,2]]
queries = [3]
```

### **Output:**  
```plaintext
[0]
```

### **Explanation:**  
- The **top-left cell (5) is already ≥ 3**, so we **cannot move** and gain **0 points**.  

---

## **Constraints**  
- `m == grid.length`  
- `n == grid[i].length`  
- `2 <= m, n <= 1000`  
- `4 <= m * n <= 10⁵`  
- `k == queries.length`  
- `1 <= k <= 10⁴`  
- `1 <= grid[i][j], queries[i] <= 10⁶`  

---

## **Discussion**  

### **Approach 1: Min-Heap + BFS (Optimized Approach)**  
- **Use a Min-Heap** to efficiently process the smallest grid values first.  
- **Sort queries** in increasing order to process them efficiently.  
- **Use BFS (Breadth-First Search)** to expand cells **only when needed**.  
- **Store results** for each query and return `answer`.  

### **Time Complexity:**  
- **O(m * n log(m * n) + k log k)** → Efficient for large grids.  

### **Space Complexity:**  
- **O(m * n + k)** → Stores visited cells and results.  

---

## **🔥 Optimized Solution Using Python**  

```python
from heapq import heappush, heappop

def maxPoints(grid, queries):
    m, n = len(grid), len(grid[0])
    answer = []
    queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])
    
    # Min-Heap for BFS
    heap = [(grid[0][0], 0, 0)]
    visited = set((0, 0))
    count = 0
    res_map = {}

    for idx, query in queries_sorted:
        while heap and heap[0][0] < query:
            _, r, c = heappop(heap)
            count += 1
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    heappush(heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
        res_map[idx] = count

    return [res_map[i] for i in range(len(queries))]
```

---

## 🎯 **How to Contribute**  
1. **Fork** the repository.  
2. Implement the solution and **test** it with multiple cases.  
3. Submit a **pull request** with a clear explanation.  

---

## 📂 **File Structure**  
```
/solutions  
   ├── max_points_grid_queries.py  
   ├── README.md  
```  

---

## 🔥 **Want to Participate?**  
- Discuss solutions in **GitHub Issues**.  
- Improve existing implementations.  

---

## 🔗 **Useful Links**  
- [LeetCode Problem](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/)  
- [Python Heapq Documentation](https://docs.python.org/3/library/heapq.html)  
- [BFS Algorithm Guide](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)  

---

💡 **Let's learn, code, and grow together! 🚀**  