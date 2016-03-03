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
        #print 'i am going...'
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
                            [0,1,0,0,0],
                            [0,1,1,1,1],
                            [0,0,0,0,0],
                            [1,1,1,1,0],
                            [0,0,0,1,0],
                         ], (0,0), (4,4))


maze2 = MazeRunner([
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ], (7,7), (0,0))


maze3 = MazeRunner([
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ], (0,5), (10,5))


maze4 = MazeRunner([
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ], (0,5), (4,5))


maze5 = MazeRunner([
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ], (0,5), (4,5))


def maze_controller(maze):

    def check_left_side():
        maze.turn_right()
        if maze.go():
            maze.turn_left()
            #print 'i can go left'
            return True
        else:
            maze.turn_left()
            return False

    def check_right_side():
        maze.turn_left()
        if maze.go():
            maze.turn_right()
            #print 'i can go right'
            return True
        else:
            maze.turn_right()
            return False

    while not maze.found():
        while maze.go():
            if maze.found():
                return maze.found()
            if check_right_side():
                maze.turn_right()
            if check_left_side():
                maze.turn_left()
            maze.go()
        while not(maze.go()):
            #print 'i am stuck'
            if check_left_side():
                #print 'i turned left'
                maze.turn_right()
            elif check_right_side():
                #print 'i turned right'
                maze.turn_left()
            else:
                #print 'i turned around'
                maze.turn_left()
                maze.turn_left()
    return maze.found()
print maze_controller(maze1), 1
print maze_controller(maze2), 2
print maze_controller(maze3), 3
print maze_controller(maze4), 4
#print maze_controller(maze5), 5

