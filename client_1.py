import socket
import threading
from server_help_funcs import *

PORT = 5678
IP = "127.0.0.1"



def connect():
    """connect the client to the server
    Returns:
        socket[socket]:
    """
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defining the socket
    my_socket.connect((IP, PORT))  # connect to the server
    print("Connected to server on port %d" % PORT)
    return my_socket


def main():

    conn_sock = connect()# connects to the server
    res = ""
    curr_dict = {}
    while res != 'q':
        res = input("HEY \n WELCOME TO YPUR PRIVATE DATABASE \n WOUKD YOU LIKE TO READ/UPDATE/EXIT - (1/2/q)    ")
        if res != 'q':
            if res == '1':# the user hasa asked to read the file
                conn_sock.send("1".encode())
                print(recv_msg(conn_sock))
            if res == '2':
                conn_sock.send("2".encode())
                print(recv_msg(conn_sock))    
                new_dict = {}
                print("Enter key:value and <ENTER>, when finished press <e> ")
                dict_part = ""
                while dict_part != ['e']:
                    dict_part = input().split(":")
                    if len(dict_part) == 2:
                        new_dict[dict_part[0]] = dict_part[1]
                conn_sock.send(dict_to_str(new_dict).encode())
                print(recv_msg(conn_sock))
    

if __name__ == '__main__':
    main()