import threading
import pickle


def conv_to_file(dicti, file_name):
    """recieves a dictionary and write it binary into a file"""
    dict_file = open(file_name, "wb")
    pickle.dump(dicti, dict_file)

def conv_to_dict(file_name):
    """recieves a file name and return a dictionary from it"""
    dict_file = open(file_name,'rb')
    object_file = pickle.load(dict_file)
    return object_file


class DATA_BASE:
    def __init__(self, path="", file_name="HORESH"):
        """file_name: the data base file name, path: we=here you want the data base to be located"""   
        if path == "":
            self.file_name = file_name
        else:
            self.file_name = path + "\\" + file_name + ".pickle" 
    
    def update_file(self, dicti):
        """recieves a new dictionary and replace the current one in the file return a dictionary with false if it was alrea"""
        try:
            conv_to_file(dicti, self.file_name)
        except:
            print("CONVERTAION FAILED")
        
    
    def read_file(self):
        """return the file dictionary"""
        response ={"succedded": False}
        try:
            response = conv_to_dict(self.file_name)
            print("READING SUCCEEDED")
        except:
            print("READING FAILED")
        return response
        

