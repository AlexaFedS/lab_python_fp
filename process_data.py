import json
import sys
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique


path = 'data_light.json'

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(arg):
    return Unique(list(field(arg, 'job-name')), ignore_case=True)


@print_result
def f2(arg):
    return list(filter(lambda job: job.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda job: job + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = gen_random(len(arg), 100000, 200000)

    return [job + f', зарплата {salary} руб' for salary, job in zip(salary, arg)]

def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == "__main__":
    main()