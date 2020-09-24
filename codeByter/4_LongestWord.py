# Have the function LongestWord(sen) take the sen parameter being passed
# and return the largest word in the string.
# If there are two or more words that are the same length,
# return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.

# Examples
# Input: "fun&!! time"
# Output: time
# Input: "I love dogs"
# Output: love


def LongestWord(sen):
    characterList = list(sen)
    tempList = []
    for char in characterList:
        if (char.isalpha() or char.isdigit() or char == " "):
            tempList.append(char)
            pass
    newString = "".join(tempList)
    wordList = newString.split()
    maxLen = 0
    retWord = ""
    for word in wordList:
        if len(word) > maxLen:
            maxLen = len(word)
            retWord = word
            pass
        pass
    return retWord


# keep this function call here
print(LongestWord(input()))
