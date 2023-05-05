print("word scrapping")
print('''
1. search for word and its position
2. to alter the passage with word replacement
3. to know the size of the passage
4. to know number of symbols in passage
5. to quit''')

passage = input("please enter your passage: ")
symbols_to_remove = '''`~!@#$%^&*()_-+={[}]|/\:;"'<,>.?'''
passage_without_symbols = ''
for letters in passage:
    if letters not in symbols_to_remove:
        passage_without_symbols += letters
new_passage = str(passage_without_symbols).split()
symbols = ' '


def symbol(passage_, without_symbols, new_symbol):
    symbol_ = ' '
    for letter in passage_:
        if letter not in without_symbols:
            symbol_ += letter
    print(symbol_)
    new_symbol += symbol_
    print(f"number of symbols in passage: {len(new_symbol)}")


def find(passage_):
    search = input("enter a word to search: ")
    words = []
    index = []
    for letter in passage_:
        words.append(letter)
    for n in range(len(words)-1):
        if search == words[n]:
            index.append(n)
    print(index)


def replace(passage_):
    word = input("enter the word:")
    replace_ = input("enter the word to be replaced: ")
    words = []
    sentence = ' '
    for letter in passage_:
        words.append(letter)
        for n in range(len(words)):
            if word == words[n]:
                words[n] = replace_
    sentence = ' '.join(words)
    print(sentence)


def size(passage_, old, symb):
    print(f"size of the passage: {len(old)}")
    numb = 0
    for letter in passage_:
        numb += len(letter)
    print(f"number of words in the passage: {numb}")


while (i := input("enter your choice: ")) != "5":
    if i == "1":
        find(new_passage)
    elif i == "2":
        replace(new_passage)
    elif i == "3":
        size(new_passage, passage, symbols)
    elif i == "4":
        symbol(passage, passage_without_symbols, symbols)
    else:
        print("invalid")
        print('''enter valid input \n
        1. search for word and its position
        2. to alter the passage with word replacement
        3. to know the size of the passage
        4. to know number of symbols in passage
        5. to quit''')
