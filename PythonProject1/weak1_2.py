import time
import random

list_source = ['Кот','Рандом','Понимание','Честь','Превосходство','Сыр','Канапе','Микротранзакции','Арнольд','Мир','Пёс','Ловушка','Мина','Рыба','Анчоус']
my_list = []
my_dict = {'Кот' : 0}
intdict = 2
count2 = 0
for i in range(0,999999):
    my_list.append(list_source[random.randint(0,len(list_source)-1)])
start = time.time()
count1 = my_list.count('Кот')
finish = time.time()
print(f'Столько вхождений кот в список {count1} поиск за время {finish - start}с')
start = time.time()
for i in range(0,999999):
    if my_list[i] in my_dict:
        count2 = count2 + 1
finish = time.time()
print(f'Столько вхождений кот в список {count2} поиск за время {finish - start}с')
#Столько вхождений кот в список 99740 поиск за время 0.021585702896118164с
#Столько вхождений кот в список 99740 поиск за время 1.2348744869232178с