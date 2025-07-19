import nmap
"""PortScanner() is an object in nmap module to creat scanner object"""
finder=nmap.PortScanner()

"""there is scan method in PortScanner object to scan for open ports"""

finder.scan("localhost","1-100")

"""finder.all_hosts() method in PortScanner object Returns a list of all hosts found in the scan"""

hosts=finder.all_hosts()


for host in hosts:
    """finder[host].hostname() method in PortScanner object Returns	Hostname of scanned IP"""
    print(f"host : {host} ({finder[host].hostname()})")

    """finder[host].state() method in PortScanner object Returns weater the host is (up) or (down)"""
    print(f"State: {finder[host].state()}")

    """finder[host].all_protocols() method in PortScanner object Returns a list of network protocols detected on the host"""
    protocols=finder[host].all_protocols()

    for proto in protocols:
        print(f"Protocol: {proto}")

        """finder[host][proto].keys() method in PortScanner object Returns Ports found under the protocol"""
        ports = finder[host][proto].keys()

        for port in sorted(ports):

            print(f"Port: {port}\tState: {finder[host][proto][port]['state']}")

