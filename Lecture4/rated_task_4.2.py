import sys
dani = sys.argv[1:]
dani_ob = str(dani[::-1])
print dani_ob.replace("', '", " ").replace("['", "").replace("']", "")
