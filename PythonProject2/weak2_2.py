import  time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Работа прошла за {finish - start}')
        return result
    return wrapper

class FileProcessor:
    def __init__(self,path):
        self.path = path

    @time_it
    def write_to_file(self,data):
        try:
            with open(self.path,'w') as file:
                file.write(data)
                return data
        except FileNotFoundError:
            return 'Файл не найден!'

    @time_it
    def read_from_file(self):
        try:
            with open(self.path,'r') as file:
                result = file.read()
                return result
        except FileNotFoundError:
            return 'Файл не найден!'
