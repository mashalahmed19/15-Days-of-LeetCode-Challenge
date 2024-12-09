class Solution:
    def compress(self, chars):
        write = 0  # Position to write the compressed characters
        read = 0   # Position to read characters

        while read < len(chars):
            char = chars[read]  # Current character
            count = 0

            # Count consecutive characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
