def Multiply(a,b):
    if b == 0:
        return 0
    if b == 1:
        return a
    return a + Multiply(a,b-1)

print(Multiply(5,0))
