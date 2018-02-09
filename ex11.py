import random

alphabet = [chr(i) for i in range(ord("A"),ord("Z") + 1)]

rows = []
columns = []

for i in range(100):
    row = ""
    for j in range(100):
        row += alphabet[random.randrange(len(alphabet))]
    rows += [row]

for i in range(100):
    column = ""
    for row in rows:
        column += row[i]
    columns.append(column)

with open("words.txt", "r") as text:
    words = [line.rstrip().upper() for line in text]

for row in rows:
    print row

print words
