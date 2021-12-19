import threading


class DATA_BASE:
    def __init__(self, file_name, path):
        """file_name: the data base file name, path: we=here you want the data base to be located"""     
        self.file_name = file_name
        self.path = path
        self.lock = threading.Lock()# an object that has to two statements locked and unlocked
    
    def 
    

p1 = Person("John", 36)

print(p1.name)
print(p1.age)