class TrieNode():
    def __init__(self):
        self.children = {} 
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root 
        for c in word :
            node = cur.children.get(c) 
            if node == None:
                node = TrieNode() 
                cur.children.update({c:node}) 
            cur = node 
        cur.is_end = True 


    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word :
            node = cur.children.get(c) 
            if node == None :
                return False
            cur = node 
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for c in prefix :
            node = cur.children.get(c) 
            if node == None :
                return False 
            cur = node 
        return True 
        
        