import socket
import getpass

from time import sleep
def try_to_connect(ip_addr, con_port):
    sock = socket.socket()
    sock.settimeout(1)

    print('������� ���������� � ��������')
    try:
        sock.connect((ip_addr, con_port))
    except ConnectionRefusedError as err:
        print(err)
        return False
    except TypeError:
        return False
    print('���������� �����������')

    while True:
            try:
                data = sock.recv(1024)
            except socket.timeout:
                break
            print('������� �������')
            print(data.decode())


    while True:
        msg = input('������ ���� ��������� ��� �������: ')
        print('������� ��������� ������ �������:')
        sock.send(msg.encode())
        print('������� ����������')
        if msg == 'exit':
            break
        print('������� ������ ������ �� �������:')
        try:
            data = sock.recv(1024)
        except socket.timeout:
            continue
        print('������� �������')
        print(data.decode())

    sock.close()
    return True

ip_addr= getpass.getpass(prompt = '������� IP address: ')
if ip_addr == '':
    ip_addr = '192.168.1.39'
con_port=getpass.getpass(prompt = '������� ����: ')
if con_port == '':
    con_port=13131
else:
    try:
        con_port=int(con_port)
    except:
        print('������������ ����')


logical=False
count_conn_try=0
while count_conn_try<5:
    logical=try_to_connect(ip_addr,con_port)
    if not logical:
        count_conn_try+=1
    else:
        count_conn_try=0
if count_conn_try==5:
    print('������ ����������')
