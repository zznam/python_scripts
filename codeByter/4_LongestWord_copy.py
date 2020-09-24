def LongestWord(sen):
    nw = ""
    for letter in sen:
        if letter.isalpha() or letter.isnumeric():
            nw += letter
        else:
            nw += " "
    return max(nw.split(), key=len)


# keep this function call here
print(LongestWord(input()))
