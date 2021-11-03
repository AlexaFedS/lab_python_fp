goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    result = list()
    buf = dict()
    for i in items:
        for j in args:
            try:
                buf[j] = i[j]
            except:
                pass
        result.append(buf.copy())
        buf.clear()
    print(result)
    return result

field(goods, 'title', 'color')