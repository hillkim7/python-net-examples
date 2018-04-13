# Echo server program
import socket
import sys

if len(sys.argv) < 2:
    print("%s port" % sys.argv[0])
    sys.exit()

def main(port):
    HOST = None               # Symbolic name meaning all available interfaces
    s = None
    for res in socket.getaddrinfo(HOST, port, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print('could not open socket')
        sys.exit(1)
    while True:
        conn, addr = s.accept()
        print('Connected from', addr)
        while 1:
            data = conn.recv(1024)
            if not data: break
            conn.send(data)
        conn.close()

if __name__ == '__main__':
    try:
        main(int(sys.argv[1]))
    except KeyboardInterrupt:
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        exit(0)
