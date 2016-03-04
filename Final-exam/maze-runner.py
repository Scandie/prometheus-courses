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
        print 'i am going in that direction'
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


def maze_controller(maze):

    # even if you only check side or ability to go, your runner do that in maze

    def check_left_side():
        maze.turn_right()
        print 'checked left side'
        if maze.go():
            #maze.turn_left()
            #print 'i can go left'
            return True
        else:
            print "i can't go left"
            maze.turn_left()
            return False

    def check_right_side():
        maze.turn_left()
        print 'checked right side'
        if maze.go():
            #maze.turn_right()
            #print 'i can go right'
            return True
        else:
            print "i can't go right"
            maze.turn_right()
            return False

    def fork():

        """
        Checking ability to go right and left at the same time
        """

        if check_left_side():
            maze.turn_right()
            maze.turn_right()
            maze.go()
            maze.turn_left()
            if check_right_side():
                maze.turn_right()
                maze.turn_right()
                maze.go()
                maze.turn_right()
                return True
                print 'Hmm so this is a fork...'
            else:
                return False

    def choose_longer_corridor():

        """
        choose longer corridors between left and right
        """
        print 'I am choosing my corridor'
        distance_left = 1
        maze.turn_right()
        while maze.go():
            distance_left += 1
        print 'left corridor is', distance_left, 'fields long!'
        d_l = distance_left
        maze.turn_right()
        maze.turn_right()
        while d_l != 1:
            maze.go()
            d_l -= 1
        maze.turn_right()

        distance_right = 1
        maze.turn_left()
        while maze.go():
            distance_right += 1
        print 'right corridor is', distance_right, 'fields long!'
        if distance_left > distance_right:
            print 'i choose left corridor!'
            maze.turn_right()
        else:
            print 'i choose right corridor!'
            d_r = distance_right
            maze.turn_right()
            maze.turn_right()
            while d_r != 1:
                maze.go()
                d_r -= 1
            maze.turn_right()
            maze.turn_left()







    while not maze.found():
        print fork.__doc__
        while maze.go():
            if maze.found():
                return maze.found()
            if fork():
                choose_longer_corridor()
            #if check_left_side():
                #print ''
            #if check_right_side():
                #print ''
        while not (maze.go()):
            print 'i am stuck'
            if check_left_side():
                print ''
                #maze.turn_right()
            elif check_right_side():
                print ''
                #maze.turn_left()
            else:
                print 'i turned around'
                maze.turn_left()
                maze.turn_left()
    return maze.found()


print maze_controller(maze1), 1
print maze_controller(maze2), 2
print maze_controller(maze3), 3
#print maze_controller(maze4), 4
#print maze_controller(maze5), 5
