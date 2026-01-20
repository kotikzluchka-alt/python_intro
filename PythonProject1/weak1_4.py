transactions = [
    ['Москва', 'iPhone', 100000],
    ['Москва', 'Samsung', 50000],
    ['Лондон', 'iPhone', 120000],
    ['Москва', 'iPhone', 100000], # Еще один айфон в Москве
    ['Лондон', 'Samsung', 55000],
    ['Москва', 'Samsung', 50000],
    ['Токио', 'iPhone', 110000],
]
my_dict = {}
for i in range(len(transactions)):
    if (transactions[i][0],transactions[i][1]) not in my_dict:
        my_dict[(transactions[i][0],transactions[i][1])] = transactions[i][2]
    else:
        my_dict[(transactions[i][0],transactions[i][1])] += transactions[i][2]
for i in my_dict.keys():
    print(f"{i} c суммой {my_dict[i]} \n")
