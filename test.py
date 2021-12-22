from my_base import *


db_one = DATA_BASE("C:\\Users\\cyber\\Downloads\\horesh", "test1")
my_dict = {"idot": 95, "agam": 100, "zontag": 90}
db_one.update_file(my_dict)
my_new = db_one.read_file()
print(my_new)
my_dict
db_one.update_file(my_dict)
