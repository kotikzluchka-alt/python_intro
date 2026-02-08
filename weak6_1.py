import sys
big_list = [x for x in range(1000000)]
big_gen = (x for x in range(1000000))
print(f'{sys.getsizeof(big_list)} - Размер списка\n{sys.getsizeof(big_gen)} - Размер генератора')