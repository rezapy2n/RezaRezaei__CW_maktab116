import string
def is_pangram(s):
     alphabet_set = set(string.ascii_lowercase)
     s_set = set(s.lower())
     return alphabet_set.issubset(s_set)
test_string = "The quick brown fox jumps over the lazy dog"
result = is_pangram(test_string)
print(f"Is the string a pangram? {'Yes' if result else 'No'}")