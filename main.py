with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()

def count_words():
    return len(words)

def count_letters():
    letters = {}
    for w in words:
        for c in w.lower():
            if c in letters:
                letters[c] += 1 
            else:
                letters[c] = 1 
    return letters

def print_a_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document")
    print()

    dict_letter_count = count_letters()
    list_letter_count = list(dict_letter_count)
    list_letter_count.sort()

    clean_letter_count = []
    for c in list_letter_count:
        if c.isalpha():
            clean_letter_count.append(c)
    
    for c in clean_letter_count:
        print(f"The '{c}' character was found {dict_letter_count[c]} times")
    print("--- End report ---")

print_a_report()