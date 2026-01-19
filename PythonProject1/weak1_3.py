import random
import time

target = 9561
my_list = []
for i in range(10000):
    my_list.append(random.randrange(1,10000))
my_set = {}
flag = True
start = time.time()
for i in range(10000):
    my_set[my_list[i]] = my_list[i]
for i in range(len(my_list)):
    targets = target - my_list[i]
    if targets < 0 or targets == my_list[i]:
        continue
    if targets in my_set:
        finish = time.time()
        print(f'Пара чисел {my_list[i]} и {my_set[targets]} за время {finish - start} с')
        flag = False
        break
finish = time.time()
if flag:
    print(f"Таких пар чисел нет за время {finish - start} с")
start = time.time()
flag = True
print('\n Брутфорс \n')
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] + my_list[j] == target and my_list[i] != my_list[j]:
            finish = time.time()
            print(f'Пара чисел {my_list[i]} и {my_list[j]} за время {finish - start} с')
            flag = False
            break
    if flag == False:
        break
finish = time.time()
if flag:
    print(f"Таких пар чисел нет за время {finish - start} с")