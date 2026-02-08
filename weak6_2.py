def lazy_read(file_path):
    with open(file_path,'r') as f:
        next(f)
        for line in f:
            parts = line.strip().split(',')
            order_id = int(parts[0])
            amount = int(parts[1])

            if amount > 900:
                yield {'id': order_id,'amount': amount}

lazy = lazy_read('orders.csv')

counter = 0
for order in lazy:
    print(f'Нашёл подходящий заказ {order}')
    counter += 1
    if counter > 5:
        break
print("Оброботка завершена память свободна")
