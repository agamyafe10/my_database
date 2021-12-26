from my_base import *
import threading



# creatimg the new object
db_one = DATA_BASE("", "test1")
my_dict = {"idot": 95, "agam": 100, "zontag": 90}
# db_one.update_file(my_dict)

dict_1 = {"idot": 95, "agam": 100, "zontag": 93}
dict_2 = {"idot": 95, "agam": 100, "zontag": 70}
dict_list = []
dict_list.append(my_dict)
dict_list.append(dict_1)
dict_list.append(dict_2)
trd_lst = []
for i in range(3):
    trd_lst.append(threading.Thread(target = db_one.update_file, args = (dict_list[i],)))


for t in trd_lst:
    t.start()




# db_one.update_file(my_dict)
# my_new = db_one.read_file()
# print(my_new)
# my_dict
# db_one.update_file(my_dict)
