import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def split_url(url_list,url):
    new_list = []
    for i in range(0,5):
        new_list.append(url_list[i + (url - 1) * 5])
    return new_list
def hetch_url(url):
    time.sleep(1)
    return url
if __name__ == '__main__':
    url_list = []
    for i in range(20):
        url_list.append(f'url_{i}')
    print(url_list)
    start = time.time()
    for url in url_list:
        hetch_url(url)
    finish = time.time()
    print(f'Время выполнения {finish - start}')
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executer:
        future = {executer.submit(hetch_url,url): url for url in url_list}
        print(future)
    finish = time.time()
    print(f'Время выполнения {finish - start}')
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as process_executer:
        results = list(process_executer.map(hetch_url,url_list))
    finish = time.time()
    print(f'Время выполнения {finish - start}')
