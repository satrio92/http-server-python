import socket as sock

host = '127.0.0.1'
port = 10000

server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
server.bind((host, port))
server.listen()

print('Server is listening on port ' + str(port))

while True:
    connect, address = server.accept()
    request = connect.recv(1024).decode()
    if (request.split(' ')[0] == '' or request.split(' ')[1] == '/favicon.ico'):
        continue

    method = request.split(' ')[0]
    route = request.split(' ')[1]

    print(method)
    print(route)

    if (route == '/'):
        filename = "home.html"
    elif (route == '/quotes'):
        filename = "quotes.html"
    elif (route == '/jokes'):
        filename = "jokes.html"
    elif (route == '/about'):
        filename = "about.html"


    data_buffer = ""
    data_str_wrapper = open(filename,"r")
    try:
        str += data_str_wrapper
    except Exception as e:
        print("Can't combine strings and wrappers")
        print(e)
    data_buffer += data_str_wrapper.read()
    response = 'HTTP/1.0 200 OK\r\n\r\n' + data_buffer
    connect.sendall(response.encode())
    connect.close()

server.close()
