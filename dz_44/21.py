from ipaddress import *
net = ip_network('145.125.105.101/255.255.248.0', 0)
print('.'.join(f'{x:>08b}' for x in [255, 255, 248, 0]), 'mask')
print('.'.join(f'{x:>08b}' for x in [145, 125, 105, 101]), 'ip')
print('.'.join(f'{x:>08b}' for x in [145, 125, 104, 0]), 'net')
print(net)


#1001101
#1000000