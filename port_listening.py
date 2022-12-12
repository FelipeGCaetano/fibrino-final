import os
import socket

def testeConexao(ip, port):
    conectado = False
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if connection.connect_ex(("127.0.0.1", int(port))):
        print("Porta", port, "esta fechada")
    else:
        print("Porta", port, "esta aberta")
        conectado = True
    
    while conectado == False:
        os.system("python manage.py runserver")

testeConexao("127.0.0.1", "8000")
