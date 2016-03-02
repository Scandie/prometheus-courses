
def clean_list(list_to_clean):
    found = []
    for element in list_to_clean:
        if found.count(element) < 1:
            found.append(element)
        elif isinstance(element, float) and found.count(str(element)) < 1:
            found.append(element)
    return found


print clean_list(['qwe', 'reg', 'qwe', 'REG'])
print clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
print clean_list([1, 1.0, '1', -1, 1])
print clean_list([32, 32.1, 32.0, -123])
