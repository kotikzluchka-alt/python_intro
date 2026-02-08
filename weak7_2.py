import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def squere_sum(number):
    for i in range(len(number)):
        suma = sum(i*i for i in range(number[i]))
    return suma
def squere_sum_range(number):
    suma = sum(i*i for i in range(number))
    return suma

if __name__ == '__main__':
    tasks = [5000000,5000000,5000000,5000000]
    start = time.time()
    for i in range(len(tasks)):
        squere_sum_range(tasks[i])
    finish = time.time()
    print(f'Время выполнения {finish - start}')
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executer:
        future = executer.submit(squere_sum,tasks)
        res = future.result()
    finish = time.time()
    print(f'Время выполнения {finish - start}')
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as process_executer:
        results = list(process_executer.map(squere_sum_range,tasks))
    finish = time.time()
    print(f'Время выполнения {finish - start}')
