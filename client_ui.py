from my_base import DATA_BASE
import threading




class my_ui:
    
    my_lock = threading.Lock()# 
    maxThreads = 10 # the maximum number of readers allowed
    my_sema = threading.BoundedSemaphore(maxThreads)
    def __init__(self, path="", file_name="HORESH"):
        """file_name: the data base file name, path: we=here you want the data base to be located"""   
        self.my_db = DATA_BASE(path, file_name)# the database object
        

    def run_base(self):
        res = ""
        curr_dict = {}
        while res != 'q':
            res = input("HEY \n WELCOME TO YPUR PRIVATE DATABASE \n WOUKD YOU LIKE TO READ/UPDATE/EXIT - (1/2/q)")
            if res != 'q':
                
                if res == '1':# the user hasa asked to read the file
                    if not my_ui.my_lock.locked():# if nobody updates
                        my_ui.my_sema.acquire()
                        curr_dict = self.my_db.read_file()
                        print(curr_dict)
                        my_ui.my_sema.release()
                if res == '2':
                    if not my_ui.my_lock.locked() and  my_ui.my_sema.get_value == 0:# if nobody updates
                        my_ui.my_lock.acquire()
                        curr_dict = self.my_db.read_file()
                        print(curr_dict)
                        new_dict = {}
                        print("Enter key:value and <ENTER>, when finished press <e> ")
                        while client_input != 'e':
                            dict_part = input().split(":")
                            new_dict[dict_part[0]] = dict_part[1]
                            client_input = input()
                        self.my_db.update_file(new_dict)
                    