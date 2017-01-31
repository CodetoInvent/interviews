from collections import defaultdict

def build_word_count(words):
    count = defaultdict(int)
    for word in words:
        count[word] += 1

    return count

def has_enough_count(magazine, ransom):
    for word in ransom:
        if (not word in magazine) or (magazine[word] < ransom[word]):
            return False

    return True


def has_enough_words(magazine, ransom):
    magazine_count = build_word_count(magazine)
    ransom_count = build_word_count(ransom)
    if (has_enough_count(magazine_count, ransom_count)): print "YES"
    else: print "NO"

magazine = ["give", "me", "one", "one", "one", "grand", "today", "night"] 
ransom = ["give", "one", "one", "grand", "today"] 
has_enough_words(magazine, ransom)