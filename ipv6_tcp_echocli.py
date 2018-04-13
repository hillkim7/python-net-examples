# Echo client program
import socket
import sys

if len(sys.argv) < 4:
    print("%s ip port msg" % sys.argv[0])
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])
msg = bytes(sys.argv[3], 'ascii')
s = None
for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
print('sending %d bytes' % len(msg))
s.sendall(msg)
data = s.recv(1024)
s.close()
print('%d bytes received' % len(data))
