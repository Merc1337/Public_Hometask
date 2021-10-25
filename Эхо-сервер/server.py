import socket,sys,getpass,random
#If you want to save 'print' in log file{
# orig_stdout = sys.stdout
# f = open('server_log.txt', 'w')
# sys.stdout = f
# # }


def listening(sock):
    conn, addr = sock.accept()
    print('��������� ������: ', addr)

    with open("clients.txt", 'a+') as clients:
        clients.seek(0,0)
        for line in clients:
            if addr[0] in line:
                conn.send(('Hello '+line.replace(addr[0], '')).encode())
                break
        else:
            conn.send('Enter your name!'.encode())
            username = conn.recv(1024).decode()
            clients.write('\n'+username+addr[0])

    ret=False
    msg = ''

    while True:
        print('����� ������ �� �������')
        try:
            data = conn.recv(1024)
        except (ConnectionResetError, ConnectionAbortedError) as err:
            print(err, addr)
            return
        msg = data.decode()
        print(msg)
        if msg == 'shutdown':
            ret=True
            break
        if not data:
            break
        conn.send(data)
        print('�������� ������ �������')
    conn.close()
    print('���������� �������:', addr)
    return ret


print('������ �������')
print('''��� ������� ���������� ������ ���������� ��������
��� ��������� ������� shutdown - ��������� ������''')
sock = socket.socket()



c_port = 13131
while True:
    try:
        sock.bind(('', c_port))
        print("��������� � ����� {}".format(c_port))
        break
    except OSError as oserr:
        print("{} (���� {} �����)".format(oserr,c_port))
        c_port = random.randint(1024,65535)

sock.listen(0)
print('������ ������������� �����')


ret=False
while not ret:
    ret=listening(sock)
print('��������� �������')


#If you want to save 'print' in log file{
# sys.stdout = orig_stdout
# f.close()
