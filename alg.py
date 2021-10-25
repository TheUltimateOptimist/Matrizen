import math


def komischerAlgorithmus(n, z):
    neueZahl = 0
    i = 1
    m = n
    ziffern = 0
    while m > 0:
        m = math.floor(m/10)
        ziffern += 1
    while n > 0 and i < 100:
        print("n = " + str(n))
        rest = n % 10
        print("rest = " + str(rest))
        n = n - rest
        n = n / 10
        print("n2 = " + str(n))
        if rest != z:
            neueZahl = neueZahl + rest*(10**(ziffern - i))
            print("nZ = " + str(neueZahl))
        i += 1
    return neueZahl


print(komischerAlgorithmus(1888, 8))
