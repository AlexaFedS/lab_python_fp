class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = False
        self.items = items
        self.iter = -1
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.items = self.Uniq_maker(items)

    def Uniq_maker(self, items):
        uniqlist = list()
        for i in items:
            if self.is_uniq(i, uniqlist):
                uniqlist.append(i)
        return uniqlist

    def is_uniq(self, first, second):
        if type(first) is str and self.ignore_case:
            for j in second:
                if type(j) is str:
                    if first.lower() == j.lower():
                        return False
            return True
        elif first not in second:
            return True
        return False

    def __next__(self):
        try:
            self.iter += 1
            return self.items[self.iter]
        except:
            raise StopIteration


    def __iter__(self):
        return self

data = [1, 1, 1, 2, 2, 4, 6,6]
for i in Unique(data):
    print(i)