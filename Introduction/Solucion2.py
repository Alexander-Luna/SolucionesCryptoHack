from pwn import *
import json

HOST ="socket.cryptohack.org"
PORT = 11112
r=remote(HOST,PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hash):
    request=json.dumps(hash).encode()
    r.sendline(request)

print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())


request={
    "buy":"flag"
}

json_send(request)
response=json_recv()
print(response)