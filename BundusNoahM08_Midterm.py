def get_input(filename: str) -> None:
    with open(filename, 'w') as file:
        get_input: str = input("Input the first word of your sentence: ").lower()
        get_input = get_input.capitalize()
        file.write(f"{get_input}\n")
        while str(get_input) != "":
            get_input = input("Input the next word of your sentence, or input nothing to end the sentence: ").lower()
            file.write(f"{get_input}\n")

def data_cleaner(filename: str) -> list:
    """Read words from a file and return them as a list."""
    words: list = []
    with open(filename, 'r') as file:
        for line in file:
            word: str = line.strip()
            if word:
                words.append(word)
    return words

def display_words_and_stats(words: list) -> None:
    """Display the words and their statistics."""
    count: int = len(words)

    if count > 0:
        print("Your sentence is:", end="")
        for word in words:
            print(f" {word}", end="")
        print(".")
    else:
        print("No words were entered.")

    print(f"There are {count} words in the sentence.")

def main() -> None:
    """Main function to execute the program."""
    filename: str = "sentence.txt"
    get_input(filename)
    words: list = data_cleaner(filename)
    display_words_and_stats(words)

main()