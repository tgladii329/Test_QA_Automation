def letter(s):
    newlist = ''
    for e in s:
        if e.isalpha():
            newlist += e
    assert newlist.isalpha()
    return newlist


r = letter("hjunk987(^ jg")
print(r)
