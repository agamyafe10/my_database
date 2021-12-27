import threading
import time
import socket
import select
from help_funcs import *
from client_ui import *

# deafault settings
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5678


server_socket = setup_socket()
open_client_sockets = []  # the sockets which currently connected to the server

my_lock = threading.Lock()# 
maxThreads = 10 # the maximum number of readers allowed
my_sema = threading.BoundedSemaphore(maxThreads)

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
            if client_request is None:
                print("[Client Disconnected Surprisingly]")
                open_client_sockets.remove(current_socket)
                continue
            if client_request == "1" and not my_ui.my_lock.locked():# if the clients want to read 
                my_sema.acquire()
                send_value(current_socket, my_db.read_file())
                my_sema.release()
            elif client_request == "2":# if the clients want to read
                if not my_lock.locked() and  my_sema._value == 10:# if nobody updates
                    my_lock.acquire()
                    send_value(current_socket,"Enter key:value and <ENTER>, when finished press <e> ")
                    new_dict = str_to_dict(recv_msg(current_socket))
                    print("Enter key:value and <ENTER>, when finished press <e> ")
                    dict_part = ""
                    while dict_part != ['e']:
                        dict_part = input().split(":")
                        if len(dict_part) == 2:
                             new_dict[dict_part[0]] = dict_part[1]
                    my_db.update_file(new_dict)
                    my_lock.release()
