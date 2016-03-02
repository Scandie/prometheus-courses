def encode_morze(message):
    morse_code = {
        "A" : "^_^^^",
        "B" : "^^^_^_^_^",
        "C" : "^^^_^_^^^_^",
        "D" : "^^^_^_^",
        "E" : "^",
        "F" : "^_^_^^^_^",
        "G" : "^^^_^^^_^",
        "H" : "^_^_^_^",
        "I" : "^_^",
        "J" : "^_^^^_^^^_^^^",
        "K" : "^^^_^_^^^",
        "L" : "^_^^^_^_^",
        "M" : "^^^_^^^",
        "N" : "^^^_^",
        "O" : "^^^_^^^_^^^",
        "P" : "^_^^^_^^^_^",
        "Q" : "^^^_^^^_^_^^^",
        "R" : "^_^^^_^",
        "S" : "^_^_^",
        "T" : "^^^",
        "U" : "^_^_^^^",
        "V" : "^_^_^_^^^",
        "W" : "^_^^^_^^^",
        "X" : "^^^_^_^_^^^",
        "Y" : "^^^_^_^^^_^^^",
        "Z" : "^^^_^^^_^_^",
        " " : "_______"
    }
    message = message.upper()
    coded_message = ''
    for letter in message:
        if not(letter.isalpha()) and letter != " ":
            message = message.replace(letter, '')
    print message
    i = 0
    while i != len(message):
        coded_message += morse_code[message[i]]
        if i != len(message)-1 and message[i] != ' ' and message[i+1] != ' ':
            coded_message += '___'
        i += 1
    return coded_message


print encode_morze('1.23')
print encode_morze('SOS--..-')
print encode_morze('Morze code')
print encode_morze('Prometheus')