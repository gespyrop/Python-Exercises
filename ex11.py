import random

alphabet = [chr(i) for i in range(ord("A"),ord("Z") + 1)]

rows = []

for i in range(100):
    row = ""
    for j in range(100):
        row += alphabet[random.randrange(len(alphabet))]
    rows += [row]

for row in rows:
    print row
