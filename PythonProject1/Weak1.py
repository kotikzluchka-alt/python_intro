import random
import time

start = time.time()
my_list =[] #//1.51 секунда на вставку
my_set = set() #//1.93 секунда на вставку
k = 0
for i in range(0,1000000):
    my_list.append(random.randrange(0,1000000))
for i in range(0,1000000):
    my_set.add(random.randrange(0,1000000))
start = time.time()
k = my_list.index(25)
finish = time.time()
print(f'время выполнения: {finish-start} c и 25 по адресу {k}')
start = time.time()
k = 25 in my_set
finish = time.time()
print(f'время выполнения: {finish-start} c и 25 есть {k}')
#время выполнения: 0.0010890960693359375 c и 25 по адресу 38230
#время выполнения: 2.86102294921875e-06 c и 25 есть False
#вывод хоть я и нашёл более быструю функцию поиска в коллекции но это всё равно намного медленнее чем искать элемент в множестве