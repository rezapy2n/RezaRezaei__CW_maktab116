words = ["apple", "banana", "cherry", "date", "elderberry"]

count_vowels = lambda word: sum(1 for char in word.lower() if char in "uoiae")

sorted_words = sorted(words, key=count_vowels, reverse=True)

print(sorted_words)