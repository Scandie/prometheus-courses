import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

x_kup = '-la' * (x - 1)
kup = 'la' + x_kup
if int(y) != 0:
    y_kup = ' ' + (kup + ' ') * y
    y_kup = y_kup[0:-1]
else:
    y_kup = ''

if z == 1:
    y_kup += '!'
else:
    y_kup += '.'


print 'Everybody sing a song:' + y_kup
