def func(*args):
    l = list(set(args))
    l.sort()
    return print(l[1])

func(4, 3, 3, 1, 1, 7, 1)
