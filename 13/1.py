k = 0
from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240')
for ip in net:
    print(ip)
    if bin(int(ip)).count('1') % 2 == 0:
        k += 1
print(k)