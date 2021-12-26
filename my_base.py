import threading
import pickle


def conv_to_file(dicti, file_name):
    """recieves a dictionary and write it binary into a file"""
    # my_dict = {"idot": 95, "agam": 100, "zontag": 90}
    dict_file = open(file_name, "wb")
    pickle.dump(dicti, dict_file)
    print("CONVERTING TO FILE SUCCESSEDED")

def conv_to_dict(file_name):
    """recieves a file name and return a dictionary from it"""
    dict_file = open(file_name,'rb')
    object_file = pickle.load(dict_file)
    print("CONVERTING TO DICTIONARY SUCCESSEDED")
    return object_file


class DATA_BASE:
    def __init__(self, path="", file_name="HORESH"):
        """file_name: the data base file name, path: we=here you want the data base to be located"""   
        if path == "":
            self.file_name = file_name
        else:
            self.file_name = path + "\\" + file_name + ".pickle" 
        # self.lock = threading.Lock()# an object that has to two statements locked and unlocked
        # self.readers = 0 
        # self.wating_list = []# a list of a the waiting 
    
    def update_file(self, dicti):
        """recieves a new dictionary and replace the current one in the file return a dictionary with false if it was alrea"""
        try:
            conv_to_file(dicti, self.file_name)
            print("CONVERTAION SUCCEEDED")
        except:
            print("CONVERTAION FAILED")
        #         response = {"succedded": True} 
        # flag = False  
        # while not flag:
        #     if self.readers == 0:# if nobody reasds the file   
        #         flag = True         
        #         self.lock.acquire()# prevents from other threads to change the file
        #         conv_to_file(dicti, self.file_name)
        #         response = {"succedded": True} 
        #         self.lock.release()
        #         break
        # return response
    
    def read_file(self):
        """return the file dictionary"""
        response ={"succedded": False}
        try:
            response = conv_to_dict(self.file_name)
            print("READING SUCCEEDED")
        except:
            print("READING FAILED")
        return response
        # if not self.lock.locked() and self.readers < 10: # if nobody writes to the file and there are less than 10 readers
        #     self.readers += 1
        #     response = conv_to_dict(self.file_name)
        #     self.readers -= 1
        # return response


