def func(count=3, word=3, theend=0):
    if theend == 0:
        return ("la-"*(word-1)+"la"+"."+'\n')*count
    else:
        return ("la-"*(word-1)+"la"+"!"+'\n')*count
r = func(theend=1)
print(r)
