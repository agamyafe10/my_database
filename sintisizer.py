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




# dicti = {10: 20, 30: 40, 50: 60}
# conv_to_file(dicti, "idot.pickle")
# new_dicti = conv_to_dict("idot.pickle")
# print(new_dicti)