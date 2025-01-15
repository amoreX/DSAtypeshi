class Node:
    def __init__(self,val=None):
        self.val= val
        self.nodes={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=Node()
    
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.nodes:
                tempnode=Node(char)
                node.nodes[char]=tempnode
            node=node.nodes[char]
        node.is_end=True

    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.nodes:
                return False
            node=node.nodes[char]
        return node.is_end

    def startsWith(self,prefix):
        node=self.root
        for char in prefix:
            if char not in node.nodes:
                return False
            node=node.nodes[char]
        return True

trie=Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.startsWith("app"))
