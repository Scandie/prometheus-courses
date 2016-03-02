#ticket_diapason_1 = int(raw_input('enter ticket diapason start : '))
#ticket_diapason_2 = int(raw_input('enter ticket diapason end : '))
import sys
ticket_diapason_1 = int(sys.argv[1])
ticket_diapason_2 = int(sys.argv[2])

last_3_numbers_sum = 0
first_3_numbers_sum = 0
count = 0

while int(ticket_diapason_1) < int(ticket_diapason_2) + 1:
    current_ticket = str(ticket_diapason_1).zfill(6)
    first_3_numbers = current_ticket[:3]
    last_3_numbers = current_ticket[3:]

    print str(first_3_numbers), '   ', str(last_3_numbers)

    for i in range(3):
        first_3_numbers_sum += int(first_3_numbers[i])
        last_3_numbers_sum += int(last_3_numbers[i])

    if first_3_numbers_sum == last_3_numbers_sum:
        print first_3_numbers_sum, ' --- ', last_3_numbers_sum, '!!!'
        count += 1

    print 'curr lucky tickets count:', count
    first_3_numbers_sum = last_3_numbers_sum = 0
    ticket_diapason_1 += 1

print 'final tickets count: '
print count
