# -*- coding: utf-8 -*-
our_number = int(raw_input("vvedit' chyslo : \n", ))
print our_number
print str(bin(our_number))[2:]
our_str = str(bin(our_number))[2:]
our_str = our_str.replace('0', ')')
our_str = our_str.replace('1', '(')
print our_str
while not(our_str == ''):
    if our_str.count('(') != our_str.count(')'):  # Первірка на однакову кількість дужок
        print 'NO'
        break
    sym = our_str.find('(')                       # Шукаємо позицію першої відкритої дужки '('
    if sym == 0:                                  # Якщо вона не на початку послідовності, то NO
        our_str = our_str.replace('(', '')        # Якщо на початку, то видаляємо її і шукаємо першу закриту дужку ')'
        sym = our_str.find(')')                   # Якщо вона є, то видаляємо її теж. якщо її немає, то NO
        if sym == -1:                             # В іншому випадку, якщо дужок більше немає, то YES
            print 'NO'
            our_str = ''
        else:
            our_str = our_str.replace(')', '')
            if our_str == '':
                print 'YES'
    else:
        print 'NO'
        our_str = ''
