3169. Count Days Without Meetings

"""
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days
"""

class Solution:
    def minAvailableDuration(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        i = 0
        while i < len(meetings):
             start, end = meetings[i]
             j = i + 1
             while j < len(meetings) and meetings[j][0] <= end:
                 end = max(end, meetings[j][1])
                 j += 1
             if end - start >= days:
                 return start
             i = j
             days -= (end - start)
             if days <= 0:
                  return -1

Solution:
     