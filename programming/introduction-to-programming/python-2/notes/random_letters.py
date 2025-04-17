import random

letters = ['a'] * 100
print(letters)
b_loc = random.randint(0, 99)
letters[b_loc] = 'b'
print(letters)
letters = "".join(letters)
print(letters)

print("Looking for b...")
pos = 0
while letters[pos] != 'b':
    pos += 1
    print("Not yet at b")
print("Found b at position", pos)