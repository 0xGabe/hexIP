import socket, struct, sys

if len(sys.argv) != 2:
    print("[-] How to use -> python3 hexIP.py list.txt")
else:
    with open(sys.argv[1],'r') as data_file:
        for line in data_file:
            data = line.split()
            list = data[1].replace('local_address', '').split(':')
            if list[0] != '':
                hexIP = int(list[0], 16)
                hexPORT = int(list[1], 16)
                print(str(socket.inet_ntoa(struct.pack("<L", hexIP)))+':'+str(hexPORT))