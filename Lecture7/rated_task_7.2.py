class Student(object):
    course_information = {'exam_max': 30,
                          'lab_max': 7,
                          'lab_num': 10,
                          'k': 0.61
                          }

    def __init__(self, name, conf=course_information):
        self.conf = conf
        self.name = name
        self.lab_list = []
        for i in range(conf['lab_num']):
            self.lab_list.append(0)
        self.exam = 0
        print

    def make_lab(self, m, n=None):
        if n is None and self.lab_list.index:
            n = self.lab_list.index(0)
        else:
            if m > self.conf['lab_max']:
                self.lab_list[n] = self.conf['lab_max']
            else:
                self.lab_list[n] = m
        return self

    def make_exam(self, m):
        if m > self.conf['exam_max']:
            self.exam = self.conf['exam_max']
        else:
            self.exam = m
        return self

    def is_certified(self):
        sum = 0
        flag = False
        for item in self.lab_list:
            sum += item
        if (sum + self.exam) / self.conf['k'] >= 100:
            flag = True
        return sum + self.exam, flag


conf = {
    'exam_max': 30,
    'lab_max': 7,
    'lab_num': 10,
    'k': 0.61,
}
oleg = Student('Oleg', conf)
oleg.make_lab(1)
oleg.make_lab(8, 43)
"""
oleg.make_lab(1)
oleg.make_lab(10,7)
oleg.make_lab(4,1)
oleg.make_lab(5)
oleg.make_lab(6.5)
oleg.make_exam(32)
print oleg.is_certified()
oleg.make_lab(7,1)
print oleg.is_certified()
"""
