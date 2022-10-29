try:
    file = open('Scripts/File.txt', 'r')
    fileR = file.read()
    if fileR == '':
        raise Exception
    print(fileR)
except FileNotFoundError:
    print('Файла нету')
except Exception:
    print('Файл пуст')
else:
    file.close()