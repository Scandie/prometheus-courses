import random
import time
def make_sudoku(size):
    """
    :param size:
    :return:
    """
    curr_time = time.time()
    my_rows = []
    sudoku = []
    j = 1
    while len(my_rows) != size**2:
        current_row = []
        for i in range((size**2)):
            number = i+j
            if number > size**2:
                number = number-size**2
            current_row.append(number)
        j += 1
        my_rows.append(current_row)
    random_row = random.choice(my_rows)
    sudoku.append(random_row)
    my_rows.remove(random_row)


    for i in range(size**2-1):
        flag = False
        point = sudoku[len(sudoku)-1][0]
        point_1 = point + size
        while flag == False:
            if point_1 > size**2:
                point_1 -= size**2
            for row in my_rows:
                if row[0] == point_1:
                    sudoku.append(row)
                    my_rows.remove(row)
                    flag = True
            point_1 += 1
    #for row in sudoku:
        #print row
    return sudoku
print make_sudoku(3)
