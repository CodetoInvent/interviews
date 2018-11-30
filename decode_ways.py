# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# 
# Example 1:
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


def decode_ways(str):

	if not str: return 0

	return helper(str, 0)


def helper(str, index):
	
	ways = 0
	if index >= len(str):
		return ways + 1

	if index <= len(str)-2:
		if str[index] == '0': return
		i = int(str[index:index+2])

		if i >= 1 and i <= 26:
			ways += helper(str, index+2)

	i = int(str[index])

	if i >= 1 and i <= 9:
		ways += helper(str, index+1)

	return ways


print decode_ways('2626')