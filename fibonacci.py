"""
Fibonacci implementation using TDD (Test First)
Pair: peruth arishaba and natasha justine
"""

def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
