from scapy.all import *

IP = '127.0.0.1'
PORT = 80

def detect():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP, PORT))
    s.listen(256)
    while True:
        revdata = ""
        try:
           c, addr = s.accept()
           t = threading.Thread(target=handletcp, args=(c,addr))
           t.start()
        except socket.error as exc:
            log("Error: " + str(exc))
    s.close()

detect()