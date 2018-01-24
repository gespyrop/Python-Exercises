lower = [chr(i) for i in range(ord("a"), ord("z") + 1)]
upper = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
alphabet = lower + upper

def rot13(character):
    if character in alphabet:
        if character == character.upper():
            if ord(character) + 13 <= ord(upper[-1]):
                return chr(ord(character) + 13)
            else:
                return chr(ord(character) + 13 - len(upper))
        else:
            if ord(character) + 13 <= ord(lower[-1]):
                return chr(ord(character) + 13)
            else:
                return chr(ord(character) + 13 - len(lower))
    else:
        return character #ROT13 affects only letters!

sentence = raw_input("\nInsert sentence: ")

new_sentence = ""

for letter in sentence:
    new_sentence += rot13(letter)

print "\nROT13:", new_sentence

