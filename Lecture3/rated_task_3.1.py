import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

naibilsha_storona = None
mensha_storona_1 = None
mensha_storona_2 = None

if a > b:
    naibilsha_storona = a
    mensha_storona_1 = b
else:
    naibilsha_storona = b
    mensha_storona_1 = a

if c > naibilsha_storona:
    mensha_storona_2 = naibilsha_storona
    naibilsha_storona = c
else:
    mensha_storona_2 = c

suma_menshih_storin = float(mensha_storona_2) + float(mensha_storona_1)

if naibilsha_storona <= 0 or mensha_storona_1 <= 0 or mensha_storona_2 <= 0:
    print 'not triangle'
elif naibilsha_storona == mensha_storona_1:
    print 'triangle'
elif float(naibilsha_storona) >= float(suma_menshih_storin):
    print 'not triangle'
else:
    print 'triangle'

