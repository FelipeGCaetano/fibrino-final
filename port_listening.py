import socket
import subprocess
from aviso_queda import enviar_email

def testeConexao(ip, port):
    while True:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        if connection.connect_ex((ip, int(port))):
            enviar_email()
            print(subprocess.run(["python", "manage.py", "runserver"], shell=True))
        else:
            pass
    
if __name__ == '__main__':
    testeConexao("127.0.0.1", "8080")
