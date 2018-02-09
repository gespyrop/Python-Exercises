import random

alphabet = [chr(i) for i in xrange(ord("A"),ord("Z") + 1)]

rows = []
columns = []

for i in xrange(100):
    row = ""
    for j in xrange(100):
        row += alphabet[random.randrange(len(alphabet))]
    rows += [row]

for i in xrange(100):
    column = ""
    for row in rows:
        column += row[i]
    columns.append(column)

with open("words.txt", "r") as text:
    words = [line.rstrip().upper() for line in text]

inSquare = []

for word in words:
    for row in rows:
        if word in row and word not in inSquare:
                inSquare.append(word)
                break

for word in inSquare:
    words.remove(word)

for word in words:
    for column in columns:
        if word in column and word not in inSquare:
                inSquare.append(word)
                break

print "\n"
for row in rows:
    print row

if len(inSquare):
    print "\nThe square contains the following words:", ",".join(inSquare)
else:
    print "\nThe square contains none of the words!"
