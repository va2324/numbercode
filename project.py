# Initializes the lists of lowercase letters for each number on the phone keypad.
two = ["a", "b", "c"]
three = ["d", "e", "f"]
four = ["g", "h", "i"]
five = ["j", "k", "l"]
six = ["m", "n", "o"]
seven = ["p", "q", "r", "s"]
eight = ["t", "u", "v"]
nine = ["w", "x", "y", "z"]

# Compares letters in word to each list and adds corresponding number to a string.
def code(word):
    str = ""
    for char in word:
        if char in two:
            str += "2"
        elif char in three:
            str += "3"
        elif char in four:
            str += "4"
        elif char in five:
            str += "5"
        elif char in six:
            str += "6"
        elif char in seven:
            str += "7"
        elif char in eight:
            str += "8"
        elif char in nine:
            str += "9"
    return str

word = input("Please enter your word: ")
word = word.lower()

numbercode = code(word)
print(numbercode)