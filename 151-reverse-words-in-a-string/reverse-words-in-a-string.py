class Solution:
    def reverseWords(self, s):
        #Splitting the string into words, ignoring extra spaces
        words = s.split()
        #Reversing the list of words and join with a single space
        return ' '.join(words[::-1])
