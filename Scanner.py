import socket
import re
# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern to extract the number of ports you want to scan. 
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port number range.
port_min = 0
port_max = 65535
# Basic header
print("\n****************************************************************")
print("\nHey! Welcome to my port scanner! This is a simple tool that allows you to scan a target IP for open ports.")
print("\n****************************************************************")

open_ports = []
# Asking user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nEnter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    print("Enter the range of ports you want to scan in format:)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

# Basic socket port scanning
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            open_ports.append(port)

    except:
        pass

for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")