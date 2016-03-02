import sys

message = str(sys.argv[1])
decoded_message = ''
final_message = ''
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

message = message.replace(' ', '')
message = message[:(len(message) - (len(message) % 5))]

for i in range(len(message)):
    if message[i].islower():
        i = 'a'
    else:
        i = 'b'
    decoded_message += i

for i in range(len(decoded_message)+1):
    if i % 5 == 0:
        final_message += alphabet[key.find(decoded_message[(i-5):i])]

print final_message[1:]
