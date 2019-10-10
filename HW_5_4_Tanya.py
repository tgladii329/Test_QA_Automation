'''5_4_1'''
l = [2**n for n in range(0,20)]
print(l)

'''5_4_2'''
l1 = [4,78,34,10,5]
l1 = [e % 3 for e in l1]
print(l1)

'''5_4_3'''
l2 = ["ghj", 67, "#!67", 55,"55", 0]
l2 = [e for e in l2 if type(e) is int]
print(l2)

'''5_4_4'''
l3 = ["ghj", 67, "#!f85", 55, "44h", "f34 !!h"]
l3 = [e for e in l3 if type(e) is str]

def letter(s):
    newlist = ''
    for e in s:
        if e.isalpha():
            newlist += e
    return newlist

l3 = [letter(el) for el in l3]
print(l3)

