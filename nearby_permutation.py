
nearby = {
    'a': ['b1', 'c1', 'd1'],
    'b': ['c2', 'd2', 'e2'],
    'c': ['d3', 'e3', 'f3']
}

word = 'abc'

def permutations(word, index, output, result):
    if index == len(word): 
        result.add(output)
        return
    
    nearby_chars = nearby[word[index]]
    for char in nearby_chars:
        permutations(word, index+1, output+char, result)

    return result


print permutations(word, 0, '', set())

