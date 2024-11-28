class Solution:
    def longestCommonPrefix(self, strs):
        # If the list is empty, returning an empty string
        if not strs:
            return ""

        # Finding the shortest string in the list
        shortest = min(strs, key=len)

        # Comparing characters of the shortest string with all others
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]  # Returning prefix up to the mismatch

        return shortest  # If no mismatch, the shortest string is the prefix
