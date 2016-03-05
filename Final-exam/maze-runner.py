
def print_maze(maze, x, y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '


class MazeRunner(object):
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1, 0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze) - 1 \
                or y > len(self.__maze) - 1 \
                or x < 0 or y < 0 \
                or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print 'i am going in that direction'
        print_maze(self.__maze, self.__x, self.__y)
        return True

    def turn_left(self):
        left_rotation = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self

    def turn_right(self):
        right_rotation = {
            (1, 0): (0, 1),
            (0, -1): (1, 0),
            (-1, 0): (0, -1),
            (0, 1): (-1, 0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self

    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]


maze1 = MazeRunner([
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
], (0, 0), (4, 4))

maze2 = MazeRunner([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
], (7, 7), (0, 0))

maze3 = MazeRunner([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
], (0, 5), (10, 5))

maze4 = MazeRunner([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
], (0, 5), (4, 5))

maze5 = MazeRunner([
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
], (0, 5), (4, 5))

maze6 = MazeRunner([
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
], (7, 0), (2, 7))


def maze_controller(maze):
    from random import randint
    # left and right sides in MazeRunner class are inverted so it is a little bit confusing :)
    # but my functions in controller named right, so if you checked right side and wanna go there
    # you should turn.left() and backwards for the other side.

    def check_left_side():

        """
        checking ability to go left
        """
        maze.turn_right()
        #print 'checked left side'
        if maze.go():
            maze.turn_right()
            maze.turn_right()
            maze.go()
            maze.turn_right()
            # print 'i can go left'
            return True
        else:
            #print "i can't go left"
            maze.turn_left()
            return False

    def check_right_side():

        """
        checking ability to go right
        """
        maze.turn_left()
        #print 'checked right side'
        if maze.go():
            maze.turn_right()
            maze.turn_right()
            maze.go()
            maze.turn_left()
            # print 'i can go right'
            return True
        else:
            #print "i can't go right"
            maze.turn_right()
            return False

    def backward_step():

        """
        make one backward step
        """
        #print 'a step backward'
        maze.turn_left()
        maze.turn_left()
        if maze.found():
            return maze.found()
        maze.go()
        maze.turn_left()
        maze.turn_left()

    while not maze.found():

        while maze.go():
            backward_step()
            if maze.found():
                return maze.found()
            maze.go()
            rand = randint(1, 3)
            #print 'is this a fork?'
            if check_right_side():
                if check_left_side():

                    if rand == 1:
                        maze.turn_left()
                        #while maze.go():
                            #maze.go()
                    elif rand == 2:
                        maze.turn_right()
                        #while maze.go():
                            #maze.go()
                    elif rand == 3:
                        while maze.go():
                            maze.go()
            #if check_left_side():
                rand = randint(1, 2)
                if rand == 1:
                    maze.turn_left()
                    #while maze.go():
                         #maze.go()
                else:
                     maze.go()
            #if check_right_side():
                rand = randint(1, 2)
                if rand == 1:
                    maze.turn_right()
                    #while maze.go():
                         #maze.go()
                else:

                    maze.go()


        while not (maze.go()):
            #print 'i am stuck'
            if check_left_side():
                maze.turn_right()
                break
            elif check_right_side():
                maze.turn_left()
                break
            else:
                #print 'i turned around'
                maze.turn_left()
                maze.turn_left()
                break
        #maze.go()
    return maze.found()


print maze_controller(maze1), 1
print maze_controller(maze2), 2
print maze_controller(maze3), 3
print maze_controller(maze4), 4
print maze_controller(maze5), 5
print maze_controller(maze6), 6
