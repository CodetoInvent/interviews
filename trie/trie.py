

class Node(object):

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        current = self.root
        
        for i in range(len(word)):
            char = word[i]
            if char not in current.children:
                node = Node()
                current.children[char] = node

            current = current.children[char]

        current.endOfWord = True

    def search(self, word):
        current = self.root

        for i in range(len(word)):
            char = word[i]
            if char in current.children:
                current = current.children[char]
            else:
                return False

        return current.endOfWord

    def r_search(self, word, partial):
        return self.recursive_search(self.root, word, 0, partial)

    def recursive_search(self, node, word, index, partial):
        if index == len(word):
            if node.endOfWord or partial: return node
            else: return None

        char = word[index]
        if char in node.children:
            child = node.children[char]
            return self.recursive_search(child, word, index + 1, partial)
        else:
            return None

    def traversal(self, node, entries, word):
        if node.endOfWord: entries.append(word)
        
        for i in node.children.keys():
            child = node.children[i]
            self.traversal(child, entries, word + i)
        return entries

    def prefix_search(self, prefix):
        search = self.r_search(prefix, True)
        if search: return self.traversal(search, [], prefix)

        return None

    def delete_step(self, node, word, index):
        if len(word) == index:
            node.endOfWord = False 
            return len(node.children.keys()) == 0

        if word[index] in node.children:
            char = word[index]
            child = node.children[char]
            delete = self.delete_step(child, word, index + 1)
            if delete: node.children.pop(char)
            return len(node.children.keys()) == 0
        else:
            return True


    def delete(self, word):
        return self.delete_step(self.root, word, 0)





t = Trie()
t.insert_word('Hello')
t.insert_word('Helloo')
t.insert_word('Yolo')
# print t.search('hell')
# print t.r_search('Hello', False)
print t.prefix_search('Hel')
print t.delete('Hello')
print t.root.children



