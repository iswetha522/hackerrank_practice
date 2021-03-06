# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to 
# uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format

# A single line containing a string S.

# Constraints
# 0 < len(s) <= 1000

# Output Format

# Print the modified string S.
# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".
def swap_case(s):
    if len(s) <= 1000 and len(s) > 0:
        new_arr = []
        separator = ''
        for char in s:
            if char.isupper():
                char = char.lower()
                new_arr.append(char)
            else:
                char = char.upper()
                new_arr.append(char)
        s = separator.join(new_arr)      
    return s

swapped_string = swap_case('HackerRank.com presents "Pythonist 2"')
print(swapped_string)