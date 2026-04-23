# Method 2: Using a loop
def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Method 3: Using reversed() and join()
def reverse_string_reversed(s):
    return ''.join(reversed(s))

# Method 4: Using recursion
def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    return reverse_string_recursive(s[1:]) + s[0]
