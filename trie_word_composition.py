


class Node:

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word):
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = Node()

            current = current.children[i]

        current.end = True

    def exists(self, word):
        current = self.root
        for i in word:
            if i not in current.children: return False
            current = current.children[i]
        return True



dictionary = ['hello', 'wa', 'bottle', 'yo', 'cool', 'water']
word = 'waterbottle'

t = Trie()
for i in dictionary: t.insert(i)

current = t.root
prefixes = []
for i in range(len(word)):
    c = word[i]
    if c in current.children:
        current = current.children[c]
    else: break

    if current.end: prefixes.append(word[:i+1])

print prefixes

for i in prefixes:
    suffix = word[len(i):]
    if t.exists(suffix): print 'Found it! ' + i + '-' + suffix