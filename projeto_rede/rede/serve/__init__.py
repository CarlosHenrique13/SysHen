def servidor(area):
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "127.0.0.1" #127.0.0.1
    porta = 8291

    msg = "Enviando mensagem para o cliente ola"

    s.bind((host,porta))
    s.listen(1)
    while True:
        c, e = s.accept()
        try:
            area.insert(0.0,f"Conectado com {e}")
        except:
            print(f"Conectado com {e}")
        c.send(msg.encode('ascii'))
        c.close()
