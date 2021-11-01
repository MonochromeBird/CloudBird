#!/usr/bin/python3 
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)

while True:
	with s.accept() as connection:
		data = connection.recv(1024)
	handle(data)