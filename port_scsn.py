import socket


port_output=[]
def port_scan(ip_input):

    ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]

    for port in ports:  

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        result = sock.connect_ex((ip_input, port))
        if result == 0:
            port_output.append(port)
        else:
            pass
        sock.close()

    return port_output
        
print(port_scan("185.188.104.10"))