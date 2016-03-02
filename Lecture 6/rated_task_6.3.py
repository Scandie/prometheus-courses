def saddle_point(matrix):
    my_tuple = ()
    for k in range(len(matrix[0])):                # kil'kist' stovpchikiv matrici, prohodumo kojen po cherzi
        matrix_column = []
        #print "column number is :", k
        for i in range(len(matrix)):               # perebir vsih elementiv
            for j in range(len(matrix[i])):
                if j == k:                                # yaksho nomer elemnta ryadka = nomeru stovpa
                    matrix_column.append(matrix[i][j])    # robymo masiv z usima elementamy stovpchyka
                    if len(matrix_column) == len(matrix):
                        #print matrix_column
                        for s in range(len(matrix)):                        # perebyraemo kojen ryadok matrici
                            #print max(matrix_column), min(matrix[s])
                            if max(matrix_column) == min(matrix[s]):              # shukaemo sidlovu tochku
                                #print "COUNT", matrix[s].count(min(matrix[s]))
                                count = matrix[s].count(min(matrix[s]))
                                my_tuple = (s, matrix[s].index(min(matrix[s])))
                                #print 'YES', s, matrix[s].index(min(matrix my_tuple
    if my_tuple and count == 1:
        return my_tuple
    else:
        return False


print saddle_point([[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]])
print saddle_point([[5,5,5], [5,5,6], [5,4,5]])
print saddle_point([[13]])
print saddle_point([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]])
print saddle_point([[0,0,0],[2,1,2],[1,0,1]])
