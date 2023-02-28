import os

from netmiko import ConnectHandler

user = os.getenv("USER")
password = os.getenv("MY_PASS")

iosv_l2_s1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.77.134",
    "username": user,
    "password": password,
    "port": 32769,
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command("show ip int brief")
print(output)
