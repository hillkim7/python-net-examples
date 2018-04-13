# Python3 simple network programs

## Examples

### TCP server/client
* tcp echo server
```bash
python tcp_echoserv.py 5001
```
* tcp echo client
```bash
python tcp_echocli.py 127.0.0.1 5001 ABCDEF
```

### UDP server/client
* udp echo server
```bash
python udp_echoserv.py 5001
```
* udp echo client
```bash
python udp_echocli.py 127.0.0.1 5001 ABCDEF
```

### IPv6 TCP server/client
A Windows 7 supports IPv6 by default.  
A peer to peer communication between Windows PCs is possible without any special network device.  
The 'netsh interface ipv6 show address' shows IPv6 address.
* tcp echo server
```bash
python ipv6_tcp_echoserv.py 5001
```
* tcp echo client
```bash
python ipv6_tcp_echocli.py fe80::d0fd:dcb6:eeae:3729 5001 ABCDEF
```
