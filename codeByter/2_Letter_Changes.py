# Have the function LetterChanges(str) take the str parameter being
# passed and modify it using the following algorithm. Replace every letter
# in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
# Examples
# Input: "hello*3"
# Output: Ifmmp*3
# Input: "fun times!"
# Output: gvO Ujnft!
import string
ALPHABET = string.ascii_lowercase


def LetterChanges(str):
    # code goes here
    ret = ""
    for i in range(len(str)):
        # for each character, 
        # if it's contained in alphabet then new character is the following it
        try:
            isUpper = str[i].isupper()
            curIdx = ALPHABET.index(str[i].lower())
            newCharIdx = (curIdx+1) % len(ALPHABET)
            newChar = ALPHABET[newCharIdx]
            if isUpper:
                newChar = newChar.upper()
                pass
            pass
        except:
            newChar = str[i]
            pass
        # capitalize (a, e, i, o, u)
        newChar = newChar.replace("a", "A").replace("e", "E").replace("i", "I").replace("o", "O").replace("u", "U")
        ret+=newChar
        pass
    return ret


# keep this function call here
print(LetterChanges(input()))
