def is_palindrome(s):
# Remove non-alphanumeric characters and convert to lowercase
    filtered_s = ""
    for char in s:
        if char.isalnum():
            filtered_s += char.lower()
    
    # Check if the filtered string is the same when reversed
    return filtered_s == filtered_s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  
print(is_palindrome("race a car"))  
print(is_palindrome(" "))  
print(is_palindrome("hih"))
print(is_palindrome("Hello"))
