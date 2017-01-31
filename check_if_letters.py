

word = 'Zbcdefg'

UPPER_CASE = (97, 122)
LOWER_CASE = (65, 90)

within_range = lambda r, char: ord(char) >= r[0] and ord(char) <= r[1]


def rotate(char, n):
  if within_range(UPPER_CASE, char):
    start, end = UPPER_CASE
  elif within_range(LOWER_CASE, char):
    start, end = LOWER_CASE
  else: return char

  # n %= 26
  code = ord(char)
  rotated = start + n-1 if code + n > end else code + n
  return unichr(rotated)

# print ''.join(map(lambda x: rotate(x, 2), 'ABCDef,gh'))

message = 'Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg'

original_signature = 'Your friend, Alice'
encrypted_signature = message.split('-')[-1]

# print ''.join(map(lambda x: rotate(x, 0), original_signature))
for i, v in enumerate(encrypted_signature):
  if not v.isalpha(): continue

  start, end = UPPER

print encrypted_signature

# print  ord('z') - ord('a')