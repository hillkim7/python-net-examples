# Echo server program
import socket
import sys

if len(sys.argv) < 2:
    print("%s port" % sys.argv[0])
    sys.exit()

def main(port):
    HOST = '0.0.0.0'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Listen', port)
    sock.bind((HOST, port))
    while True:
        data, addr = sock.recvfrom(1024)
        print('data from', addr)
        print('echo %d bytes' % len(data))
        sock.sendto(data, addr)

if __name__ == '__main__':
    try:
        main(int(sys.argv[1]))
    except KeyboardInterrupt:
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        exit(0)
