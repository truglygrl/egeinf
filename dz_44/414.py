"""from ipaddress import *
for mask in range(33):
    net = ip_network(f'186.153.196.175/{mask}', 0)
    print(net, net.netmask)"""
print(*[x for x in range(18)], sep=', ')

