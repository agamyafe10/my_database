import threading
from sintisizer.py import *

class DATA_BASE:
    def __init__(self, path="", file_name):
        """file_name: the data base file name, path: we=here you want the data base to be located"""     
        self.path = path
        if path != "":
            self.file_name = file_name + ".pickle\\" + path
        else:
            self.file_name = file_name + ".pickle"
        self.lock = threading.Lock()# an object that has to two statements locked and unlocked
        self.readers = 0 
    
    def update_file(dict):
        """recieves a new dictionary and replace the current one in the file return a dictionary with false if it was alrea"""
        response = {"succedded": False}   
        if self.readers == 0 # if nobody reasds the file            
            self.lock.acquire()# prevents from other threads to change the file
            trans_to_file(dict, self.file_name)
            response = {"succedded": True} 
            self.lock.release()
        return response
    
    def read_file():
        """return the file dictionary"""
        response = {}
        if not self.lock.locked() and self.readers < 10: # if nobody writes to the file and there are less than 10 readers
            self.readers += 1
            response = conv_to_dict(self.file_name)
            self.readers -= 1
        return response


