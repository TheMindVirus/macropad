#!/usr/bin/python3
#pip3 install pyserial
import socket, serial

s = None
t = None
running = True

def main():
    global running
    reconnect()
    while running:
        serve()

def reconnect():
    global s, t
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.bind(("0.0.0.0", 80))
    s.listen(socket.SOMAXCONN)
    if t and t.is_open:
        t.close()
    t = serial.Serial("/dev/ttyACM0", 115200)
    if not t.is_open:
        t.open()

def serve():
    global s
    try:
        c, d = s.accept()
        m, n = c.recvfrom(1500)
        response = stream(m)
        c.sendto(response, d)
        c.close()
    except Exception:
        print("Something")
        reconnect()

def stream(request):
    global t
    response = b""
    try:
        #t.write(request)
        #response = t.read()
        n = t.write(b"GET\r\n");
        t.flush();
        print(n)
        for i in range(0, n):
            t.read()
        headers = t.read_until(b"\r\n\r\n")
        headers = headers[headers.find(b"HTTP"):]
        tokens = headers.replace(b"\r", b"").split(b"\n")
        length = 0
        for i in range(0, len(tokens)):
            if b"Content-Length" in tokens[i]:
                length = int(tokens[i].split(b":")[1].replace(b" ", b""))
        print(length)
        #print(headers)
        response = headers
        for i in range(0, length):
            response += t.read()
        print(response)
    except Exception:
        pass
    return response

if __name__ == "__main__":
    main()
    #reconnect()
    #data = bytearray()
    #t.write(b"\xFF\xEC") #Ctrl+D?
    """
    t.write(b"HTTP\r\n")
    headers = t.read_until(b"\r\n\r\n")
    tokens = headers.replace(b"\r", b"").split(b"\n")
    length = 0
    for i in range(0, len(tokens)):
        if b"Content-Length" in tokens[i]:
            length = int(tokens[i].split(b":")[1].replace(b" ", b""))
    print(headers)
    print(length)
    data = headers
    for i in range(0, length + 4):
        data += t.read()
    print(data)
    """
