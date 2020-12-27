#Python and Telnet Network Automation, configuring DHCP
#SID: 1705828
import getpass, sys, telnetlib

  #Router Host
  HOST = "172.16.1.1"

  #Telnet login
  user = raw_input("Enter username: ")
  password = getpass.getpass()
  tn = telnetlib.Telnet(HOST)

  #Entering username
  tn.read_until("Username: ")
  tn.write(user + "\n")

  #Entering password
  if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

  #Config Terminal (\n meaning "enter")
  tn.write("config terminal \n")

  #DHCP config
  #exluding addresses
  tn.write("ip dhcp excluded-address 192.168.21.1 192.168.23.1 \n")

  #configuring dhcp for vlan 21 pool
  tn.write("ip dhcp pool Vlan21DHCP \n")
  tn.write("network 192.168.21.0 255.255.255.0 \n")
  tn.write("default-router 192.168.21.1 \n")
  tn.write("exit \n")

  #configuring dhcp for vlan 23 pool
  tn.write("ip dhcp pool Vlan23DHCP \n")
  tn.write("network 192.168.23.0 255.255.255.0 \n")
  tn.write("default-router 192.168.23.1 \n")
  tn.write("exit \n")

  #closing telnet session
  print tn.close()
