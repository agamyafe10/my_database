# from my_base import *
# import threading
# from client_ui import *


# ui_new = my_ui("", "test1")
# trd_lst = []
# t1 = threading.Thread(target=ui_new.run_base, args=('2'))
# t2 = threading.Thread(target=ui_new.run_base, args=('1'))
# t1.start()
# t2.start()

def dict_to_str(my_dict):
    my_str = ""
    for key in my_dict.keys():
        my_str += key + ":" + my_dict[key] + ', '
    return my_str
def str_to_dict(my_str):
    my_str = my_str.split(', ')
    new_dict = {}
    for i in range(len(my_str)-1):
        current = my_str[i].split(':')
        new_dict[current[0]] = current[1]
    return new_dict 


my_dic = {'1':'agam', '2': 'ofir'}
str_dic = dict_to_str(my_dic)
print(str_dic)
print(str_to_dict(str_dic))