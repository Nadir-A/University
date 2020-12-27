#SID 1705828
#Configuring DHCP pools using Netmiko

from netmiko import Netmiko

# establishing the DHCP server/router
R1 = {
    "host": "172.16.1.1",
    "username": "admin",
    "password": "admin",
    "device_type": "cisco_ios",
}

# DHCP configuration commands
DHCP_commands = [
    "ip dhcp exlcluded address 192.168.21.1 192.168.23.1",
    "ip dhcp pool Vlan21DHCP",
    "network 192.168.21.0 255.255.255.0",
    "default-router 192.168.21.1",
    "ip dhcp pool Vlan23DHCP",
    "network 192.168.23.0 255.255.255.0",
    "default-router 192.168.23.1",
]

# connecting to R1 using SSH
net_connect = Netmiko(**R1)

# Configuring DHCP using DHCP_commands
print ()
print (net_connect.send_config_set(DHCP_commands))
output = net_connect.send_config_set(DHCP_commands)

# disconnecting from R1 SSH
net_connect.disconnect()

print(output)
print()
