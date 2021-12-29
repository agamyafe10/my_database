import threading
import time
import socket
import select
from server_help_funcs import *
from client_ui import *

# deafault settings
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5678


server_socket = setup_socket(SERVER_IP, SERVER_PORT)
open_client_sockets = []  # the sockets which currently connected to the server

my_lock = threading.Lock()# 
maxThreads = 10 # the maximum number of readers allowed
my_sema = threading.BoundedSemaphore(maxThreads)
my_db = DATA_BASE("", "test1")# creating the database
flag = False
print("Started Server Listening Operation...")
while not flag:
    r_list, w_list, x_list = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in r_list:
        if current_socket is server_socket:  # if it is a new client
            (new_socket, address) = server_socket.accept()
            print("new socket connected to server: ", new_socket.getpeername())
            open_client_sockets.append(new_socket)
        else:
            client_request = recv_msg(current_socket)# recieves the client request
            if client_request is None:# clients diconnects 
                print("[Client Disconnected Surprisingly]")
                open_client_sockets.remove(current_socket)
                continue
            if client_request == "1" and not my_lock.locked():# clients wants to read 
                my_sema.acquire()
                send_value(current_socket, dict_to_str(my_db.read_file()))
                my_sema.release()
            elif client_request == "2":# clients want to update
                if my_sema._value == 10:# if nobody reads
                    my_lock.acquire()
                    send_value(current_socket, dict_to_str(my_db.read_file()))# sends the current dictionary
                    new_dict = str_to_dict(recv_msg(current_socket))# recieves the updated dict from client        
                    my_db.update_file(new_dict)# updates the dictionary
                    send_value(current_socket, "UPDATE SUCCEED")
                    my_lock.release()
