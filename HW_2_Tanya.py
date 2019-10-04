phrase = input("Your message: ")
y = len(phrase)
print(y, y % 2, y // 2, sep='\n')

if y % 2 == 0:
    z = y // 2
    print(phrase[z:], phrase[0:z], sep='')
else:
    z = y // 2 + 1
    print(phrase[z:], phrase[0:z], sep='')