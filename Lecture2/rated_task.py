import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

F = (1.0 / (c * math.sqrt(2.0 * math.pi))) * math.exp(-(((a - b) ** 2.0) / (2.00 * c ** 2.0)))

print F




