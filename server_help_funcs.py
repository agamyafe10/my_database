import socket


SERVER_IP = '127.0.0.1'
SERVER_PORT = 5678

def setup_socket():
	"""
	Creates new listening socket and returns it
	Recieves: -
	Returns: the socket object
	"""
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# defining the basic socket settings
	server_socket.bind((SERVER_IP, SERVER_PORT))# defining the socket with our details
	server_socket.listen(5)# limting the number of clients can connect
	print("Listening for connections on port %d" % SERVER_PORT)
	return server_socket


def recv_msg(conn):
    """recieves a socket and returns the data recieved as a string
    """
    try:
        data = conn.recv(2048).decode()
        print("Server Response: " + data)
        return data
    except:
        print("ERROR WHILE GETTING CLIENT'S REQUEST")


def send_range(conn, dict):
	"""uses the global variable rANGE_NUM in oreder to send the range to the client
	"""

	conn.send((from_num + '-' + to_num + '-' + TARGET).encode())


def dict_to_str(conn, dict):
    my_str = ""
    for i in range(len(dict)):
        my_str += str(i.key()) + ":" + str(i.value()) + ', '
    return my_str

def str_to_dict(conn, my_str):
    my_str = my_str.split(', ')
    new_dict = {}
    for i in range(len(my_str)):
        current = my_str[i].split(':')
        new_dict[current[0]] = current[1]
    return new_dict 

def send_value(conn, my_str):
    conn.send(my_str.encode())
	