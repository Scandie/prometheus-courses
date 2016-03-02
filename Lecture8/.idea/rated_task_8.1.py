class CombStr:

    def __init__(self, my_string):
        self.my_string = my_string

    def count_substrings(self, length):
        i = 0
        uniqe_list = []
        if length > len(self.my_string):
            return 0
        else:
            while i != (len(self.my_string) - length + 1):
                tmp = self.my_string[i:length+i]
                if not (uniqe_list.count(tmp)) and tmp:
                    uniqe_list.append(tmp)
                i += 1
            return len(uniqe_list)

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0
