import os

# -=1=- ОБЩАЯ ИНФОРМАЦИЯ
cwd = os.getcwd()
file_dir = os.path.dirname(os.path.abspath(__file__))
migrations = os.listdir(file_dir)

print('Текущая рабочая директория: ', cwd)
print('Папка, в которой расположена программа: ', file_dir)
print('Всего файлов в папке с программой: ', len(migrations))


# -=2=- ОПРЕДЕЛЕНИЕ КОЛИЧЕСТВА SQL ФАЙЛОВ
sql_files_list = []
with open('sql_files_list.txt', 'w', encoding='utf8') as db:
    for fformat in migrations:
        if fformat.endswith('.sql'):
            db.write(fformat)
            sql_files_list.append(fformat)          
print('Из них файлов них в формате SQL: ', len(sql_files_list))
# print(sql_files_list)


# -=3=- ПОДГОТОВКА РЕЕСТРА АДРЕСОВ SQL ФАЙЛОВ
files_adress = list()
n =0
for f_adress in sql_files_list:
    files_adress.append(file_dir + "\\" + sql_files_list[n])
    n +=1
# print(files_adress)

# -=4=- ЦИКЛ ПОИСКА

def search():
    request = input('введите критерий поиска: ')
    result = []
    result_n = []
    for adress in files_adress:
        file_path = adress 
        with open(file_path, 'r') as f:
            if request in f.read():
                result.append(file_path)
            else:
                result_n.append(file_path)
    print(result)
    print('файлов, содержащих запрос: ', len(result))
    print('файлов, не содержащих запрос: ', len(result_n))
    print('всего проверено файлов: ', len(result) + len(result_n))