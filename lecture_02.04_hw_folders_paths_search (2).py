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
sql_files_adresses = list()
with open('sql_files_adresses.txt', 'w', encoding='utf-8') as fa:
    n =0
    for f_adress in sql_files_list:
        adress_line = file_dir + "\\" + sql_files_list[n]
        sql_files_adresses.append(adress_line)
        fa.write(adress_line)
        n +=1
# print(sql_files_adresses)
print(len(sql_files_adresses))

# -=4=- ЦИКЛ ПОИСКА

def search():
    result = list()
    while True:
        request = str(input('введите критерий поиска: '))
        for adress in sql_files_adresses:
            file_path = adress
            with open(adress, 'r', encoding='cp1251') as f:
                text = f.read()
                if request not in text:
                    del sql_files_adresses[sql_files_adresses.index(adress)]
        print(len(sql_files_adresses))
        print(sql_files_adresses)
##        print(result)
##        print('файлов, содержащих запрос: ', len(result))
##        print('файлов, не содержащих запрос: ', len(result_n))
##        print('всего проверено файлов: ', len(result) + len(result_n))


# del sql_files_adresses[sql_files_adresses.index(adress)]
