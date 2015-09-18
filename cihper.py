message = input("REGGAWS SI NOTXARB")
translated = ''

i = len(message) - 1
while i >= 0:
    print(i, translated)
    translated = translated + message[i]
    i = i - 1

print(translated)


