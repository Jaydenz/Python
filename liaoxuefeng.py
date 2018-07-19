def func(m):
    m[0] = 20
    m = [4, 5, 6]
    return m

l = [1, 2, 3]
func(l)
print('l =', l)