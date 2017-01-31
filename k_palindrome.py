
string = 'abbaa'
revrse = ''.join(reversed(string))
k = 1

i = j = 0
counter = 0
while i < len(string) and j < len(string):
    if string[i] == revrse[j]:
        i, j = i+1, j+1
        continue

    print string[i], revrse[j]
    counter+=1
    j+=1

print counter