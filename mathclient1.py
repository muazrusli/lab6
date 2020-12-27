import socket

ClientSocket = socket.socket()
host = '192.168.43.178'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))
Response = ClientSocket.recv(1024).decode()
print(Response)

while True:
    print (' L - Logarithmic \n S - Square Root \n E - Exponential \n T - Terminate')
    Input = input('Choose a function : ')
    
    if Input == 'L' :
        option = "log"
        value = input('Value : ')
        base = input('Base : ')
        l = option + '.' + value + '.' + base
        ClientSocket.send(str.encode(l))
    elif Input == 'S':
        option = "sq"
        value = input('Value : ')
        value2 = "0"
        s = option + '.' + value + "." + value2
        ClientSocket.send(str.encode(s))
    elif Input == 'E':
        option = "exp"
        value = input('Value : ')
        value2 = "0"
        e = option + '.' + value + "." + value2
        ClientSocket.send(str.encode(e))
    elif Input == "T":
        option = "ter"
        ClientSocket.send(str.encode(option))
        print ('Thank you!! \n')
        ClientSocket.close()
    else :
        print ('Invalid funtion! Try Again \n')
        
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()
