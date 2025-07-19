
import socket

target="localhost"
ports=range(1,1000)
for port in ports:
    obj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    obj.settimeout(1)
    response=obj.connect_ex((target,port))
    if response ==0:
        print(f"port {port} is oppen")
    obj.close()

