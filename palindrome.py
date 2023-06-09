def is_palindrome(s):

    reverse_s = s[::-1]
    return True if s == reverse_s else False

def func(s):

    # Check if word is already a palindrome
    if is_palindrome(s):
        return -1
    # Get length of the string
    n = len(s)
    # Define count of removed characters
    rcc = 0
    # Edge case of n = 1
    if n == 1:
        return - 1
    # We only have to iterate through the lef half of the string (+ the middle element if odd)
    for i in range(round(n/2) + n % 2):
        # Check if there is a mismatch in the characters
        if s[i] != s[n-i-1]:
            # start by edge case where you can seemingly remove both left and right but one of them throws off sequence
            if (s[i+1] == s[n-i-1]) & (s[i] == s[n-i-2]):
                # check if after removing s[i] sequency still works in next step
                if s[i+2] == s[n-i-2]:
                    # remove s[i]
                    s = s[:i] + s[i+1:]
                    removed_char = i
                # Otherwise try with RHS
                else:
                    if i > 0:
                        s = s[:n-i-1] + s[n-i:]
                    else:
                        s = s[:n-i-1]
                    removed_char = n-i-1
            # Check if removing s[i] solves the issue
            elif s[i+1] == s[n-i-1]:
                # remove s[i]
                s = s[:i] + s[i+1:]
                removed_char = i
            # Otherwise check if removing the right character solves the problem
            elif s[i] == s[n-i-2]:
                # Formatting of string slightly different if we are removing the last character
                if i > 0:
                    s = s[:n-i-1] + s[n-i:]
                else:
                    s = s[:n-i-1]
                removed_char = n-i-1
            # Finally, if neither of the above is true there is no solution
            else:
                return -1  
            if is_palindrome(s):
                return removed_char
            else:
                return -1
                
            

input_test_1 = "aaab"
print(f"test one results {func(input_test_1)}")
input_test_2 = "aaaba"
print(f"test two results {func(input_test_2)}")
input_test_3 = "a"
print(f"test two results {func(input_test_3)}")
input_test_4 = "abba"
print(f"test one results {func(input_test_4)}")
input_test_5 = "zbccxba"
print(f"test one results {func(input_test_5)}")
input_test_6 = "baaa"
print(f"test one results {func(input_test_6)}")
input_test_7 = "abca"
print(f"test one results {func(input_test_7)}")
hard_edge_case = "hgygsrlfcwnssnwcwflrsgygh"
print(f"test hard edge results {func(hard_edge_case)}")
