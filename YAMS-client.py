import socket

host = '127.0.0.1'
port = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('Tastati START pentru a incepe o sesiune noua sau STOP pentru a incheia sesiunea.')
while True:
    message = input() #salvez mesajul trimis de catre jucator in variabila message
    client_socket.send(message.encode()) #transmit mesajul codificat serverului
    mesaj_primit = client_socket.recv(500) #primesc mesajul serverului
    if('CLOSE SESSION' in mesaj_primit.decode()): #daca in mesajul serverului primesc si string-ul 'CLOSE SESSION' afisez doar tabelul final si inchid sesiunea
        print(mesaj_primit.decode().replace('CLOSE SESSION', ''))
        client_socket.close()
        break
    else:
        print(mesaj_primit.decode())

