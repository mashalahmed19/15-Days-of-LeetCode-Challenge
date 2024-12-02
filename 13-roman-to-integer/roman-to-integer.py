class Solution:
    def romanToInt(self, s):
        #Defining the values of each Roman numeral
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        #Iterating through the string in reverse
        for char in reversed(s):
            current_value = roman_values[char]
            
            #If the current value is less than the previous, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            #Updating the previous value
            prev_value = current_value
        
        return total
