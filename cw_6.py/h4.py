def is_palindrome(word):
    
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned_word == cleaned_word[::-1]

def find_palindromic_words(filename):
    palindromic_words = []
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if len(word)>2 and is_palindrome(word):
                    palindromic_words.append(word)

    num_palindromic = len(palindromic_words)
    return num_palindromic, palindromic_words

def main():
    filename = "filepalindrom.txt"  
    num_palindromic, palindromic_words = find_palindromic_words(filename)

    print(f"Number of palindromic words: {num_palindromic}")
    print(f"Palindromic words: {', '.join(palindromic_words)}")

if __name__ == "__main__":
    main()