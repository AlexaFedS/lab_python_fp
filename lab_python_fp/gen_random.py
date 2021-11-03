import random

def gen_random(num_count, begin, end):
    if num_count != 0:
        mas = [random.randint(begin, end) for i in range(num_count)]
        print(mas)
    return 0

gen_random(5, 2, 10)