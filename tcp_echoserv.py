# TCP echo server program
import socket
import sys

if len(sys.argv) < 2:
    print("%s port" % sys.argv[0])
    sys.exit()

def main(port):
    HOST = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Listen', port)
    s.bind((HOST, port))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('Connected from', addr)
        while 1:
            data = conn.recv(1024)
            if not data: break
            print('echo %d' % len(data))
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
