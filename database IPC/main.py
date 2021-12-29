import threading
import pickle
import socket
import time

FILENAME = 'database'
MAX_THREADS = 10

threadLimiter = threading.BoundedSemaphore(MAX_THREADS)
lock = threading.Lock()

# change ip
IP, PORT   = socket.gethostname(), 9214

def write(ins):
    outfile = open(FILENAME,'wb')
    pickle.dump(ins,outfile)
    outfile.close()
def read():
    infile = open(FILENAME,'rb')
    out = pickle.load(infile)
    infile.close()
    return out

# Handles every new client
def handler(client, address):
    while True:
        # -----------------------------------
        ans = client.recv(512).decode()
        if ans[0] == 'P':
            print(f'disconncted {address}')
            lock.acquire()
            write(ans[1:])
            lock.release()
            client.send("W".encode())
        elif ans[0]=="G":
            lock.acquire()
            out = read()
            lock.release()
            out = "D" + str(out)
            client.send(out.encode())
            print(f'{address} recived the database value')
        else:
            print("Incorrect Input")
            client.send("E".encode())


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(1)
    print("Running")

    while True:
        try:
            client, address = sock.accept()
            print(f"connected to client {address}")

            thr = threading.Thread(target=handler, args=(client, address))
            thr.start()
        except:
            continue