import socket


try:
    url = input('Input URL: ')
    parts = url.split('/')
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySock.connect((parts[2], 80))
    str = 'GET %s HTTP/1.0\r\n\r\n' % url
    print(str)
    cmd = str.encode()

    mySock.send(cmd)
    count = 0
    total = 0
    while True:
        data = mySock.recv(500)
        if (len(data) < 1):
            break
        total += len(data)
        if count < 6:
            print(data.decode())
        count += 1
    mySock.close()
    print("Total characters: ", total)
    pass
except:
    print("URL Error")
    pass
