import sys
text = str(sys.argv[1].lower())

stroka = text.replace(' ', '')


pryam = stroka
obern = stroka[::-1]

print pryam
print obern

if pryam == obern:
    print 'YES'
else:
    print 'NO'
