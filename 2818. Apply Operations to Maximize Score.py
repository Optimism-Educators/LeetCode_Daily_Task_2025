# Apply Operation to maximize Score
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