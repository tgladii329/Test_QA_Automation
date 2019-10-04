message = int(input("Enter number: "))
m = 0
while message % 2 == 0:
    m = m + 1
    print(message // 2)
    message = message // 2
print ("Q-ty of try: ", m)