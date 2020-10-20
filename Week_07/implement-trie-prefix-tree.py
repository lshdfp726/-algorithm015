class TrieNode:
    def __init__(self):
        self.mp = {}
        self.isEnd = False


class Trie:
    """
    docstring
    """
    def __init__(self):
        """
        docstring
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """
        docstring
        """
        node = self.root
        for c in word:
            if c not in node.mp:
                node.mp[c] = TrieNode()
            #指向下一个node
            node = node.mp[c]
        node.isEnd = True

        

    def search(self, word):
        node = self.root
        for c in word:
            if node.mp[c]:#当前字母存在，则找下一个
                node = node.mp[c]
            else:
                return False
        return node.isEnd
        
        
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.mp:#当前字母存在，则找下一个
                node = node.mp[c]
            else:
                return False

        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert('apple')
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))

