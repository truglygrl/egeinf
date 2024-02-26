from ipaddress import *
for mask in range(33):
    net1 = ip_network(f'120.91.176.213/{mask}', 0)
    net2 = ip_network(f'120.91.174.205/{mask}', 0)
    if net1 != net2:
        print(net1.netmask)
        print(net2.netmask)
