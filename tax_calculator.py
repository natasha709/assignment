"""
Tax calculator implementation using TDD (Test First)
Pair: peruth arishaba and natasha justine
"""

def calculate_tax(earnings):
    """
    TDD Cycle 2:
    - Now handle the 20% tax for earnings above 12000 and up to 36000.
    - Passes tests for 10000, 12000, and 13000.
    """
    if earnings <= 12000:
        return 0
    elif earnings <= 36000:
        return int((earnings - 12000) * 0.2)
    return 0  # Placeholder for next TDD cycle
