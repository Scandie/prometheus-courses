def find_fraction(number):
    if number <= 2:
        return False
    if number % 2 == 0:
        znam = number/2 + 1
        chis = number/2 - 1
        while nsd(chis, znam) != 1:
            znam += 1
            chis -= 1
    else:
        chis = number/2
        znam = number/2 + 1
    return chis, znam

def nsd(x1, x2):
    z = ''

    if int(x2) > int(x1):

        a = x2
        b = x1
    else:
        a = x1
        b = x2


    while z != 0:
        z = int(a) % int(b)
        q = (int(a)/int(b))
        nsd = b
        a = b
        b = z
    return nsd

print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)



