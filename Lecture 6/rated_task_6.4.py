def find_most_frequent(text):
    if not(text):
        return []
    else:
        my_list = []
        result_list = []
        text = text.lower()
        for letter in text:
            if not(letter.isalnum()):
                text = text.replace(letter, ' ')
            for n in range(1, len(text)):
                    text = text.replace(' '*n, ' ')
        letter = 0
        while len(text) != 0:
            while text[letter] != ' ':
                letter += 1
            my_list.append(text[:letter])
            text = text[letter+1:]
            if text.count(' ') == 0:
                my_list.append(text)
                break
            letter = 0
        my_list = sorted(my_list)
        cnt = my_list.count(my_list[0])
        for i in range(len(my_list[1:])):
            if my_list.count(my_list[i]) > cnt:
                cnt = my_list.count(my_list[i])
        for i in range(len(my_list)):
            if my_list.count(my_list[i]) == cnt and not(result_list.count(my_list[i]) == 1):
                result_list.append(my_list[i])
        return result_list


print find_most_frequent('Mike-Paul mike')
print find_most_frequent('')
print find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello")
print find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind")