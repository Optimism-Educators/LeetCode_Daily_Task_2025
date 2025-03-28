# 2503. Maximum Number of Points From Grid Queries
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
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

