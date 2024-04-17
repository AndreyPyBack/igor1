# import os
# for root, dirs, files in os.walk("NewFolder"):
#     for fn in files:
#         print(fn)
import os
import shutil
#shutil.copyfile("C:\\Users\\Андрей\\PycharmProjects\\API\\file.txt", "C:\\Users\\Андрей\\PycharmProjects\\API\\new_fol5673der\\file.txt")
# print(os.getcwd())
# os.remove('C:\\Users\\Андрей\\PycharmProjects\\API\\file.txt')
# os.chdir("..\\..\\../")
# print(os.getcwd())
# print(os.getlogin())
data = [['2001638940179228', 3922280], ['4578638940179227', 1778600],
['2001557163484689', 4035370]]
a = lambda x :[int(x[0]),str(x[1])]
print(list(map(a,data)))
# import shutil
# #shutil.copyfile("C:\\Users\\Андрей\\PycharmProjects\\API\\file.txt", "C:\\Users\\Андрей\\PycharmProjects\\API\\new_fol5673der\\file.txt")
# shutil.copyfile('C:/Users/Андрей/PycharmProjects/API/s.txt','C:/Users/Андрей/PycharmProjects/API/new_folder')