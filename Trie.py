class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.word_list = []
        
    def formTrie(self, keys):
        for key in keys:
            self.addWord(key)

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:    
            if not ch in node.children.keys():
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for ch in word:
            next_nodes = []
            for node in nodes:            
                if ch in node.children.keys():
                    next_nodes.append(node.children[ch])
                if ch == '.':
                    next_nodes.extend(node.children.values())
            nodes = next_nodes
        return any(node.isEndOfWord for node in nodes)
    
    
    def suggestionsRec(self, node, word):
        # Method to recursively traverse the trie
        # and return a whole word.
        if node.isEndOfWord:
            self.word_list.append(word)

        for a,n in node.children.items():
            self.suggestionsRec(n, word + a)
    
    def printSuggestions(self, key):
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions.
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.isEndOfWord and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)

        for s in self.word_list:
            print(s)
        return 1
      
      
# Driver Code
keys = ["hello", "dog", "hell", "cat", "a","hel", "help", "helps", "helping"] # keys to form the trie structure.
key = "hel" # key for autocomplete suggestions.

# creating trie object
t = WordDictionary()

# creating the trie structure with the
# given set of strings.
t.formTrie(keys)

# autocompleting the given key using
# our trie structure.
comp = t.printSuggestions(key)

if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")
    
/*
Output:
hel
hell
hello
help
helps
helping

*/
