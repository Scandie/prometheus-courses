def count_holes(n):
    for number in str(n):
        if number == '.':
            return 'ERROR'
    if not(isinstance(n, int) or isinstance(n, long) or isinstance(n, str))or n == '':
        return 'ERROR'
    else:
        n = str(n)
        number = 0
        if len(n) > 1:
            while n[number] == '0':
                number += 1
        n = n[number:]
        null_counter = 0
        for number in n:
            if number == '0':
                null_counter += 1
            elif number == '1':
                null_counter += 0
            elif number == '2':
                null_counter += 0
            elif number == '3':
                null_counter += 0
            elif number == '4':
                null_counter += 1
            elif number == '5':
                null_counter += 0
            elif number == '6':
                null_counter += 1
            elif number == '7':
                null_counter += 0
            elif number == '8':
                null_counter += 2
            elif number == '9':
                null_counter += 1
            elif number != '-':
                return 'ERROR'
        return null_counter


print count_holes('')



