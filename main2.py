# import os
#
# def create_folder_and_file():
#     os.makedirs("NewFolder", exist_ok=True)  # Создаёт папку, если она не существует
#     with open("NewFolder/newfile.txt", "w") as f:
#         f.write("Hello, world!")  # Записывает текст в файл
#
# create_folder_and_file()
#
# import shutil
#
# def move_file():
#     shutil.move("newfile.txt", "NewFolder/newfile.txt")  # Перемещает файл
#
# move_file()

for i in range(10):
    f = open(f"new{i}.txt",'w')