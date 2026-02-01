import pytest
import os
from weak2_2 import FileProcessor

def test_correct():
    file1 = FileProcessor('C:/Users/HONOR/Desktop/пароли и другой мусор/пайтон')
    file1.write_to_file('Я люблю собак')
    result = file1.read_from_file()
    assert result == 'Я люблю собак'
def test_uncorrect():
    file1 = FileProcessor('C:/Users/HONOR/Desktop/пароли и другой мусор/пайто')
    if os.path.exists('C:/Users/HONOR/Desktop/пароли и другой мусор/пайто'):
        os.remove('C:/Users/HONOR/Desktop/пароли и другой мусор/пайто')
    result = file1.read_from_file()
    assert result == 'Файл не найден!'



