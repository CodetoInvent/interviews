
class Node:

    def __init__(self,):
        self.end_of_word = False
        self.children = {}
        self.count = 0


class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert_word(self, word):
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = Node()
            current = current.children[i]
            current.count += 1

        current.end_of_word = True

    def find_node(self, word):
        current = self.root
        for i in word:
            if i in current.children:
                current = current.children[i]
            else:
                return None

        return current


    def prefix_search(self, prefix):
        node = self.find_node(prefix)
        if not node: return None

        words = []
        def traverse(node, children):
            if node.end_of_word: words.append(prefix + children)
            for i, v in node.children.items():
                traverse(v, children + i)

        traverse(node, '')

        return words

    def count_prefix(self, prefix):
        node = self.find_node(prefix)
        return node.count




t = Trie()

t.insert_word("Hello")
t.insert_word("Hello2")
t.insert_word("Hell")
t.insert_word("")
t.insert_word("No")
print t.prefix_search('He')
print t.count_prefix('He')
