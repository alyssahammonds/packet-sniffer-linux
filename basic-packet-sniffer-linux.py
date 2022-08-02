# https://www.uv.mx/personal/angelperez/files/2018/10/sniffers_texto.pdf

import socket


# IPv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
  print(s.recvfrom(65565)) #receive all data from socket
  
