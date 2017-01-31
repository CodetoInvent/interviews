# Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    maximum = 0
    i = j = 0
    charachters = set()
    while i < len(s) and j < len(s):
        if s[j] not in charachters:
            charachters.add(s[j])
            j += 1
            maximum = max(maximum, j - i)
        else:
            charachters.remove(s[i])
            i += 1
    return maximum




