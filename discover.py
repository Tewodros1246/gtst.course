import sys
import nmap
target=sys.argv[1]
ip_class=sys.argv[2]
if ip_class.lower()=="a":
    subnet=24
elif ip_class.lower()=="b":
    subnet=16
elif ip_class.lower()=="c":
    subnet=8
elif ip_class.lower()=="d":
    subnet=0
else:
    print("invalid class")

def finder(target_name,subnetmask):
    network=f"{target_name}/{subnetmask}"
    nn=nmap.PortScanner()
    nn.scan(hosts=network, arguments="-sn")

    hosts=nn.all_hosts()
    for host in hosts:
        print(f"Host: {host} is {nn[host].state()}")


finder(target,subnet)

