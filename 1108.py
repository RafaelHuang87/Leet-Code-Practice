"""
Solution for Leet Code 1108.
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")