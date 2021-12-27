from my_base import *
import threading
from client_ui import *


ui_new = my_ui("", "test1")
trd_lst = []
t1 = threading.Thread(target=ui_new.run_base, args=('2'))
t2 = threading.Thread(target=ui_new.run_base, args=('1'))
t1.start()
t2.start()



