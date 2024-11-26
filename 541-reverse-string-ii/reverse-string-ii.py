class Solution:
    def reverseStr(self, s, k):
        # Converting the string into a list
        s = list(s)
        
        # Processing every 2k characters
        for i in range(0, len(s), 2 * k):
            # Reversing the first k characters of the current 2k-block
            s[i:i + k] = s[i:i + k][::-1]
        
        # Converting the list back to a string & returning it
        return ''.join(s)
