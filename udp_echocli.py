# UDP echo client program
import socket
import sys

if len(sys.argv) < 4:
    print("%s ip port msg" % sys.argv[0])
    sys.exit()

port = int(sys.argv[2])
rx_port = port + 1  # set port number for receive
server_addr = (sys.argv[1], port)
msg = bytes(sys.argv[3], 'ascii')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', rx_port))
try:
    # Send data
    print('sending %d bytes' % len(msg))
    sent = sock.sendto(msg, server_addr)

    # Receive response
    data, server = sock.recvfrom(4096)
    print('%d bytes received' % len(data))

finally:
    print('closing socket')
    sock.close()
