def LetterChanges(str):
    newstr = ""
    outstr = ""
    for char in str:
        if char.isalpha():
            if char != "z":
                newstr = newstr + chr(ord(char)+1)
            else:
                newstr = newstr + "a"
        else:
            newstr = newstr + char
    print(newstr)
    for char in newstr:
        if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
            char = char.upper()
        outstr = outstr + char

    return outstr


# keep this function call here
print(LetterChanges(input()))
