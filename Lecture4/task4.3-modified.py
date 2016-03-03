our_number = int(raw_input("vvedit' chyslo : \n", ))
print our_number
print str(bin(our_number))[2:]
our_str = str(bin(our_number))[2:]
our_str = our_str.replace('0', ')')
our_str = our_str.replace('1', '(')
print our_str
while not(our_str == ''):
    sym = our_str.find('(')
    #print sym
    if sym == 0:                                  # Shukaemo index pershoi vidkritoy dujki '('
        our_str = our_str.replace('(', '')        # Yaksho index = 0, to vidalyaemo element i shukaemo pershu zakrity dujku.
        #print our_str                            # Yaksho vona e, to vidalyaemo ii tej. Yaksho ii nema to NO
        sym = our_str.find(')')                   # Yaksho index pershoi vidritoy dujki '(' != 0 to NO
        #print sym                                # V inshomu vypadku, yaksho kinchilis' elementy to YES
        if sym == -1:
            print 'NO'
            our_str = ''
        else:
            our_str = our_str.replace(')', '')
            #print our_str
            if our_str == '':
                print 'YES'
    else:
        print 'NO'
        our_str = ''