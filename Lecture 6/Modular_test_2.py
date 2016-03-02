def convert_n_to_m(x, n, m):

    if (not isinstance(x, int) and not isinstance(x, str) and not isinstance(x, long)) or x < 0 or isinstance(x, bool):
        return False
    elif isinstance(x, str) and not x.isalnum():
        return False
    elif isinstance(x, str) and x == '0'*len(x):
        return 0
    elif x == 0:
        return 0
    else:

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num_dict = {}
        for i in range(26):                      # Zapovnenn'a slovnika
            for j in range(10):
                num_dict[str(j)] = str(j)
            num_dict[str(alphabet[i])] = str(i + 10)
        #print num_dict

        #print """       PERSHA CHASTINA    (Perevedenn'a v desyatkovu systemu)      """
        x = str(x)
        x = x.upper()
        x = list(x)
        item = 0
        cnt = len(x) - 1
        sum = 0
        flag = True
        while item != len(x):
            #print x[item]
            if (x[item].isalpha()) and (int(num_dict[x[item]]) > (n-1)):
                flag = False
            #if not flag:
                #print 'flag', x[item]
            x[item] = num_dict[x[item]]
            sum += (n**cnt)*int(x[item])
            #print '16 ^', cnt, '*', x[item], ' = ', sum
            item += 1
            cnt -= 1

        x = sum
        #print x

        #print """       DRUGA CHASTINA   (Perevedenn'a v bud' yaky inshu systemu)       """
        answer = ''
        result_list = []
        result = 1
        if m == 1:
            for i in range(x):
                answer += '0'
        else:
            while result + x > 0:
                #print x, 'mod', m, '=', result
                result = x % m
                if result <= 9:
                    result_list.append(result)
                else:
                    result_list.append(alphabet[result-10])
                x /= m
                #print x, 'mod', m, '=', result
            result_list.reverse()
            #print result_list[1:]
            for item in result_list[1:]:
                answer += str(item)
        if flag:
            return answer
        else:
            return flag

print convert_n_to_m([123], 4, 3)
print convert_n_to_m("0123", 5, 6)
print convert_n_to_m("123", 3, 5)
print convert_n_to_m(123, 4, 1)
print convert_n_to_m(-123.0, 11, 16)
print convert_n_to_m("A1Z", 36, 16)
print convert_n_to_m(True, 1, 2)
print convert_n_to_m(-777, 10, 2)
print convert_n_to_m(0, 10, 2)
print convert_n_to_m(777L, 10, 2)
print convert_n_to_m('000', 10, 2)
print convert_n_to_m('ZZZZ', 35, 13)
print convert_n_to_m('qweasd', 33, 36)
print convert_n_to_m(123123123123123123123, 11, 16)
print convert_n_to_m(123123123123123123123, 10, 10)
print convert_n_to_m('bnh34521', 31, 14)
print convert_n_to_m('bnh34521', 11, 14)
