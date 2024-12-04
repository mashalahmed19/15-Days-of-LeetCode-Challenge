class Solution:
    def findTheDifference(self, s, t):
        # Use XOR to find the differing character
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)

        