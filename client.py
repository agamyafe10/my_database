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
                send_value(conn_sock, '1')
                recv_msg(conn_sock)
            elif res == '2':
                send_value(conn_sock, '2')
                old_dict = str_to_dict(recv_msg(conn_sock)) 

                c_res = ""
                while c_res != 'e':
                    c_res = input("would you like to add or update/ delete/finish (a/b/e)- ")
                    if c_res == 'a': #client wants to update or delete
                        dict_part = input("enter the key and the value you want to add or update like this (key:value)- ").split(":")
                        old_dict[dict_part[0]] = dict_part[1]
                    elif c_res == 'b':
                        dict_part = input("enter the key and the value you want to remove")
                        try:
                            old_dict.pop(dict_part)
                        except:
                            print("NONE EXISTED KEY WAS ENTERD PLEASE TRY AGAIN")
                send_value(conn_sock, dict_to_str(old_dict))
                recv_msg(conn_sock)
    
    send_value(conn_sock, 'q')


if __name__ == '__main__':
    main()