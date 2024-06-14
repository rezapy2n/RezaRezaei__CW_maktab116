import string
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.translate(str.maketrans('', '', string.punctuation))
        
        words = content.lower().split()
        return set(words)
     

     


def main():
    file_paths = ["file4.txt", "file5.txt", "file6.txt"]
    word_sets = [read_file(file) for file in file_paths]

    common_words = (set.intersection(*word_sets))
    num_common_words = (len(common_words))

    print(f"Number of common words: {num_common_words}")
    print(f"Common words: {', '.join(common_words)}")


if __name__ == "__main__":
    main()