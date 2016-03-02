
def counter(a,b):
    count = 0
    a = set(str(a))
    b = set(str(b))
    for i in a:
        for j in b:
            if j == i:
                count += 1
    return count

print counter(12345, 567)
print counter(1233211, 12128)
print counter(123, 45)
