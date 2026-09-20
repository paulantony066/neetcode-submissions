class TrieNode():
    def __init__(self):
        self.children={}
        self.isend=False
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

        
        

    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isend=True

            



    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word:
            if ch in curr.children:
                curr=curr.children[ch]
            else:
                return False
        if curr.isend:
            return True
        return False
        
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return True
        
        