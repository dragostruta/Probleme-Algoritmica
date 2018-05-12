class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
 
         # Daca isEndOfWord este True, atunci acela reprezinta sfarsitul de cuvant

        self.isEndOfWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def _charToIndex(self,ch):
        """
        Convert a char to an index
        """
        return ord(ch)-ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        poz = self.root
        length = len(word)
        for level in range(length):
            i = self._charToIndex(word[level])
 
            # daca caracterul curent nu e prezent
            if not poz.children[i]:
                poz.children[i] = TrieNode()
            poz = poz.children[i]
 
        poz.isEndOfWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        poz = self.root
        length = len(word)
        for level in range(length):
            i = self._charToIndex(word[level])
            if not poz.children[i]:
                return False
            poz = poz.children[i]
 
        return poz != None and poz.isEndOfWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        poz = self.root
        length = len(prefix)
        for level in range(length):
            i = self._charToIndex(prefix[level])
            if not poz.children[i]:
                return False
            poz = poz.children[i]
 
        return True

def teste():
        """
        Teste
        """
        obj = Trie()
        obj.insert("mama")
        assert(obj.root.children[12] != None)
        assert(obj.root.children[0] == None)
        assert(obj.root.children[12].children[0] != None)
        assert(obj.root.children[12].children[0].isEndOfWord == False)
        assert(obj.root.children[12].children[0].children[12] != None)
        assert(obj.root.children[12].children[0].children[12].children[0] != None)
        
        assert(obj.root.children[12].children[0].children[12].children[0].isEndOfWord == True)
        assert(obj.search('a') == False)
        assert(obj.search('ma') == False)
        assert(obj.search('mama') == True)
        assert(obj.search('m') == False)
        
        obj.insert("mancare")
        obj.insert("tata")
        
        assert(obj.search("t") == False)
        assert(obj.search("tata") == True)
        assert(obj.search("mancare") == True)
        assert(obj.search("manca") == False)
        
        assert(obj.startsWith("man") == True)
        assert(obj.startsWith("mam") == True)
        assert(obj.startsWith("vam") == False)
        assert(obj.startsWith("mama") == True)
        
        obj.insert("mamae")
        assert(obj.search('mama') == True)
        
        
        
        
        
        
teste()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
