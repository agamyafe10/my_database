import socket


# Change IP
SERVER_IP, PORT = socket.gethostname(), 9214

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, PORT))
    sock.settimeout(3)
    print('Connected to the server!')
    # socket server
    while True:
        num = input("1 to send data to the database\n2 to get database's data\n")
        if num == "1":
            x = input("Give data to write:\n")
            x = "P" + x
            sock.send(x.encode())
        elif num == "2":
            sock.send("G".encode())
        
        ans = sock.recv(512).decode()
        if ans[0] == "D":
            print("Data:\n")
            print(ans[1:])
        elif ans[0] == "W":
            print("Writen to the database sccussefuly!")
        elif ans[0] == "E":
            print("incorrect input, use format:\nP+data to write\nG to get")