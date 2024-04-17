# import os
#
# print(os.name)
# import os
#
# current_directory = os.getcwd()
# print("Текущая директория:", current_directory)
# import os
#
#
# os.chdir("../")
# print("Новая текущая директория:", os.getcwd())
# import os
#
# # Создание новой папки в текущей директории
# folder_name = "new_fol5673der"
# os.mkdir(folder_name)
# print("Папка создана:", folder_name)

#
# # Открываем файл для записи, что приведёт к его созданию
# f = open("newfdgile.txt", "w")
# f.write("Это новый файл.")  # Записываем текст в файл
# f.close()  # Важно закрыть файл после окончания работы
#
import os

# Получение абсолютного пути к текущей директории скрипта
# abspath = os.path.abspath(os.path.dirname(__file__))
# print(abspath)
# # Формирование пути к файлу
# path = os.path.join(abspath, "file1.txt")
# # Удаление файла
# print(path)
# os.remove(path)
# #
import os

# Список файлов и каталогов в текущей директории
# files_and_dirs = os.listdir(".")
# print(files_and_dirs)
# import os
#
# # Вывод всех файлов в текущем каталоге и подкаталогах
# for root, dirs, files in os.walk("."):
#     for filename in files:
#         print(os.path.join(root, filename))
# #
# import shutil
#
# # Копирование файла из одного места в другое
# shutil.copyfile("C:\\Users\\Андрей\\PycharmProjects\\API\\file.txt", "C:\\Users\\Андрей\\PycharmProjects\\API\\d\\s.txt")