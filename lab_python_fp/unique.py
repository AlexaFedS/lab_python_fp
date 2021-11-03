class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = False
        self.current_elements = -1
        self.items = items
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.items = self.make_unique(items)

    def make_unique(self, items):
        uniqlist = list()
        for j in items:
            if self.is_unique(j, uniqlist):
                uniqlist.append(j)
        return uniqlist

    def is_unique(self, el, ul):
        if type(el) is str and self.ignore_case:
            for i in ul:
                if type(i) is str:
                    if el.lower() == i.lower():
                        return False
            return True
        elif el not in ul:
            return True
        return False

    def __next__(self):
        try:
            self.current_elements += 1
            return self.items[self.current_elements]
        except:
            raise StopIteration

    def __iter__(self):
        return self

data = [1, 1, 1, 2, 2, 4, 6,6]
for i in Unique(data):
    print(i)