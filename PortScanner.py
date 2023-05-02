import socket

target_host = input("Enter the host to scan: ")
target_ip = socket.gethostbyname(target_host)

# Print a banner with the IP address we are about to scan
print("-" * 60)
print("Scanning target: ", target_ip)
print("-" * 60)

# Specify the range of ports to scan
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Scan each port in the specified range
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print("Port {}: Open".format(port))
    sock.close()
