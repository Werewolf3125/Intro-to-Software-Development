filename: str = "CleanText.txt"
word_list: list = []
with open(filename, 'r') as file:
    word_list = file.read().split()
    word_list.sort()
    print(word_list)

