#SID 1705828
#Configuring OSPF using parakimo and jinja template
import paramiko, jinja2, time

#router credentials
Routers = [{
    #R2
    "host": "209.165.200.232",
    "username": "admin",
    "password": "admin",
    #networks being advertisted
    "networks": [
        "172.16.1.0 255.255.255.252",
        "172.16.2.0 255.255.255.252",
        "209.165.200.232 255.255.255.248"
    ]}
    {
    #R1
    "host": "172.16.1.1",
    "username": "admin",
    "password": "admin",
    #networks being advertisted
    "networks": [
        "172.16.1.0 255.255.255.252",
        "192.168.99.0 255.255.255.0",
        "192.168.21.0 255.255.255.0",
        "192.168.23.0 255.255.255.0"
    ]}
    {
    #R3
    "host": "172.16.2.1",
    "username": "admin",
    "password": "admin",
    #networks being advertisted
    "networks": [
        "172.16.2.0 255.255.255.252",
        "192.168.4.0 255.255.255.0"
    ]}
]

#declaring template environment
ENV = Environment(loader=FileSystemLoader('.'))

#specifying jinja template
template = ENV.get_template("OSPF_Config_Template.jinja2")

#connecting to routers via SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connecting to every router previously specified
for router in Routers:


    remote_connection = ssh_client.connect(hostname=router["host"],
        username=router["username"], password=router["password"])
    remote_connection = ssh_client.invoke_shell()

    remote_connection.send("configure terminal\n")
    # this variable goes through all of the networks previously
    #  mentioned and places this in the template.
    commands = template.render(router[networks])
    # the variable commands is then executed
    remote_connection.send(commands)
    # coming out of config terminal
    remote_connection.send("end\n")
    time.sleep(1)

    #printing output
    output = remote_connection.recv(65535)
    print output

#ending SSH session
ssh_client.close
