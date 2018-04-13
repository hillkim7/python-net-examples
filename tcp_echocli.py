# TCP echo client program
import socket
import sys

if len(sys.argv) < 4:
    print("%s ip port msg" % sys.argv[0])
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])
msg = bytes(sys.argv[3], 'ascii')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print('sending %d bytes' % len(msg))
sock.send(msg)
data = sock.recv(1024)
sock.close()
print('%d bytes received' % len(data))
