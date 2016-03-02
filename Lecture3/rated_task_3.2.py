import sys

n = int(sys.argv[1])
i_0 = 0
i_1 = 1
result = 0
a = 0
for count in range(n):
    result = i_0 + i_1
    i_0 = i_1
    i_1 = result
a = result - i_0
print result - a
