# Simple HTTP Server - Alastair Cota
# This script implements a minimal HTTP server that doesn't use a TCP/IP Stack
# but instead uses print/input python natives to proxy messages over USB Serial

def ansify(data):
    sz = len(data)
    newdata = ""
    for i in range(0, sz):
        if (i == 0 or i == sz - 1) and data[i] == '\n':
            pass
        else:
            newdata += data[i]
    return newdata

ABC = \
"""
ABC
"""
ABC = ansify(ABC)
print(ABC)

data = \
"""
<title>Macropad</title>
<style>body { background: black; color: white; font-family: sans-serif; }</style>
<h1>Hello from the Macropad Web Server on USB!</h1>
"""
#""".removeprefix("\n").removesuffix("\n").replace("\n", "\r\n")
data = ansify(data)

response = \
"""
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {}
Access-Control-Allow-Origin: *

{}
"""
#""".removeprefix("\n").removesuffix("\n").replace("\n", "\r\n")
response = ansify(response)

while True:
    try:
        request = input()
        print(response.format(len(data), data))
    except:
        pass
