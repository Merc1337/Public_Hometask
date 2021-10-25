import socket
from time import sleep
#�������� ������ socket, �� ���� �������� TCP �����
sock = socket.socket()
#������������� ����������, �� ���� ����� ����� ����� ���������� ������ �������� �����
sock.setblocking(1)
#���������� ����� � ���������� � �����
sock.connect(('10.0.0.0', 9090))

# �������� ����������� ���� �������� ���������� � ���������� ��������� � ��������� ������
while True:
    # ��������� ��������� �� ������������ ����������� ������
    msg = input()
    #���������� ��������� ����� ���� ����������� � �����
    sock.send(msg.encode())
    # ���� ��������� ������������ ���� exit �� ��������� ����������� ����
    if msg == 'exit':
        break
    # ���� ������������ ���� �� exit �� ���� ��������� �� �������
    data = sock.recv(1024)
    # ������� ���������� ��������� �� ������� �������������� ������������ ��� �� ������ ����
    print(f'accepted from server:$ {data.decode()}')

# ��������� �����
sock.close()
