def super_fibonacci(n, m):
    my_list = []
    i = 1
    if n < m or n == m:
        count = 1
    else:
        while i != n+1:
            my_list.append(i)
            i += 1
        i = 0
        while i != m:
            my_list[i] = 1
            i += 1
        i = 0
        while i in range(n-m):
            my_list[i+m] = sum(my_list[i:(i+m)])
            count = my_list[i+m]
            i += 1
    return count

print super_fibonacci(2, 1)
print super_fibonacci(3, 5)
print super_fibonacci(8, 2)
print super_fibonacci(9, 3)
