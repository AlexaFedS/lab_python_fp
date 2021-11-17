goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    result = list()
    buffer = dict()
    for i in items:
        for j in args:
            try:
                buffer[j] = i[j]
            except:
                pass
        result.append(buffer.copy())
        buffer.clear()
    print(result)
    return result

field(goods, 'title', 'color')