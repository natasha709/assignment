"""
Tax calculator implementation using TDD (Test First)
Pair: peruth arishaba and natasha justine
"""

def calculate_tax(earnings):
    """
    TDD Cycle 3:
    - Now handle the 40% tax for earnings above 36000.
    - Passes all tests for the tax brackets.
    """
    if earnings <= 12000:
        return 0
    elif earnings <= 36000:
        return int((earnings - 12000) * 0.2)
    else:
        # 20% on 24000 (from 12000 to 36000), 40% on the rest
        return int((36000 - 12000) * 0.2 + (earnings - 36000) * 0.4)
