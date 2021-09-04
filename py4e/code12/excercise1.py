import socket



try:
    url = input('Input URL: ')
    parts = url.split('/')
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(parts[2])
    mySock.connect((parts[2], 80))
    str = 'GET %s HTTP/1.0\r\n\r\n' % url
    print(str)
    cmd = str.encode()

    mySock.send(cmd)
    while True:
        data = mySock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mySock.close()
    pass
except:
    print("URL Error")
    pass