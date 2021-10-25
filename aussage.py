def istPrimzahl(zahl):
    for i in range(2, zahl):
        if zahl % i == 0:
            print(i)
            return False
    return True


def testAussage(start, end):
    for i in range(start, end + 1):
        if not istPrimzahl(2**(2**i) + 1):
            print(i)
            return False
    return True


print(testAussage(1, 10))
