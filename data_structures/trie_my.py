# Python program for insert and search
# operation in a Trie


# English Alphabet: 26 characters
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        pass


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        cursor = self.root
        for char in key:
            index = self._charToIndex(char)
            if (cursor.children[index] == None):
                cursor.children[index] = self.getNode()
            cursor = cursor.children[index]
        cursor.isEndOfWord = True

    def search(self, key):
        cursor = self.root
        for char in key:
            index = self._charToIndex(char)
            if (cursor.children[index] == None):
                return False
            cursor = cursor.children[index]
        return cursor.isEndOfWord
        pass



def main():

    t = Trie()
    t.insert("the")
    t.insert("them")
    print(t.search("theo"))
    print(t.search("the"))
    print(t.search("th"))
    

if (__name__ == '__main__'):
    main()