def is_palindrome(s):

    s = s.replace(" ", "").lower()

    if s == s[::-1]:
        print("Yes")
    else:
        print("No")

input_string = "radaar"

is_palindrome(input_string)
