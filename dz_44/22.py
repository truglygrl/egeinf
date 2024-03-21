from ipaddress import *
#net = ip_network('145.125.105.101/255.255.248.0', 0)
"""print('.'.join(f'{x:>08b}' for x in [127, 98, 13, 202]))
print('.'.join(f'{x:>08b}' for x in [127, 98, 13, 192]))
"""
for mask in range(33):
    net = ip_network(f'106.73.156.100/{mask}', 0)
    print(net, net.netmask)