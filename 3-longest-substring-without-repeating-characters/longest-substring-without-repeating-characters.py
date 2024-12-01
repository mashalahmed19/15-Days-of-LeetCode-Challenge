class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_length = 0
        start = 0  # Starting index of the current substring
        
        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  
            char_index[char] = end  # Updating the character's latest index
            max_length = max(max_length, end - start + 1)
        
        return max_length
