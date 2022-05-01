class Trie(object):
    class Node:
        def __init__(self):
            self.keys = dict()
            self.end = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.keys:
                node.keys[word[i]] = self.Node()
            node = node.keys[word[i]]
            if i == len(word)-1:
                node.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(word)):
            if word[i] in node.keys:
                node = node.keys[word[i]]
            else:
                return False
            if i == len(word)-1 and node.end:
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] in node.keys:
                node = node.keys[prefix[i]]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)