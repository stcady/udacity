import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil", "stupid", "fool", "moron"]

def bleeper(word):
    pos = 0
    for char in word:
        if char in string.punctuation:
            char = '*'
        word.replace(word[pos], char)
        pos += 1
    return word

def check_line(line):
    rude_count = 0
    word_index = 0
    words = line.split(" ")
    for word in words:
        stripped_word = word.strip(string.punctuation).lower()
        if stripped_word in rude_words:
            rude_count += 1
            print(f"Rude word found: {word}")
            words[word_index] = bleeper(word)
    line = " ".join(words)
    return line, rude_count

def check_file(filename):
    with open(filename, 'r') as file:
        rude_count = 0
        lines = []
        for line in file:
            line, rude_subtotal = check_line(line)
            rude_count += rude_subtotal
            lines.append(line)
    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")
    else:
        print(f"Your file contains {rude_count} rude words.")
        with open('bleeped_copy.txt', 'w') as file_copy:
            file_copy.write("\n".join(lines))
        print("A copy of your file has been saved as 'bleeped_copy.txt'.")

if __name__ == '__main__':
    check_file('rude_words.txt') # replace with your file name