"""
    Alphabet Soup
    Have the function AlphabetSoup(str) take the str string parameter being passed 
    and return the string with the letters in alphabetical order 
    (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Examples
    Input: "coderbyte"
    Output: bcdeeorty
    Input: "hooplah"
    Output: ahhloop
    Tags: string manipulation sorting free
"""
def AlphabetSoup(str):
  letterList = list(str)
  letterList.sort()
  return "".join(letterList)

# keep this function call here 
# print(AlphabetSoup("hello"))
# print(AlphabetSoup("coderbyte"))
# print(AlphabetSoup("hooplah"))
print(AlphabetSoup(input()))