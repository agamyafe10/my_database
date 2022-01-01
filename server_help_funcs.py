import socket


def setup_socket(server_ip, server_port):
	"""
	Creates new listening socket and returns it
	Recieves: -
	Returns: the socket object
	"""
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# defining the basic socket settings
	server_socket.bind((server_ip, server_port))# defining the socket with our details
	server_socket.listen(5)# limting the number of clients can connect
	print("Listening for connections on port %d" % server_port)
	return server_socket


def recv_msg(conn):
    """recieves a socket and returns the data recieved as a string
    """
    try:
        data = conn.recv(4096).decode()
        print("Response: " + data)
        return data
    except:
        print("ERROR WHILE GETTING CLIENT'S REQUEST")



def dict_to_str(my_dict):
    my_str = ""
    for key in my_dict.keys():
        my_str += key + ":" + my_dict[key] + ', '
    return my_str

def str_to_dict(my_str):
    my_str = my_str.split(', ')
    new_dict = {}
    for i in range(len(my_str)-1):
        current = my_str[i].split(':')
        new_dict[current[0]] = current[1]
    return new_dict 

def send_value(conn, my_str):
    conn.send(my_str.encode())
	