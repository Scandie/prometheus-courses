class SuperStr(str):

    def is_palindrom(self):
        if not(isinstance(self, str)):
            return False
        else:
            self.replace(' ', '')
            self = self.lower()
            if self == self[::-1] or self is '':
                return True
            else:
                return False

    def is_repeatance(self, s):
        if not(isinstance(s, str)):
            return False
        else:
            if len(s)>len(self):
                return False
            else:
                test = self
                while len(test) > len(s) and self.find(s) == 0 and s != '':
                    test = test[len(s):]
                if test != s or s == '':
                    return False
                else:
                    return True

s = SuperStr('')
print s.is_repeatance('') # True
s1 = SuperStr('mystring1Gnirtsym')
print s1.is_palindrom()
