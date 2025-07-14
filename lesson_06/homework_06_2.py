word = ''
i = False
while i is False:
    word = input("Please enter your word with letter h: ")
    if len(word) != 0:
        for letter in word:
            if letter in ['h', "H"]:
                i = True
                break
print(word)
