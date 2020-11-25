# -------------------------
# P O R T    S C A N N E R
# ------------------------

# Anthony Bale
# Version 1.1
# Last updated 11/06/2020
# This script was made for XYZ to test for open ports on a network
# This script takes an input of a network address with a subnet, takes a port number from a txt file
# and scans a network to show which IP addresses have that port open.


# Imports
import ipaddress
import socket
from datetime import datetime
import time
import win32evtlogutil
import win32evtlog


# Check Port Numbers between 0 and 65335
def port_checker(port):
    if port in range(1, 65336):
        return True
    else:
        return False


# log to event viewer
def event_viewer(ip):
    EVT_APP_NAME = "IP Addresses"
    EVT_ID = 1998
    EVT_CATEG = 9876
    EVT_STRS = ip
    EVT_DATA = b"Open ports"

    win32evtlogutil.ReportEvent(EVT_APP_NAME,
                                EVT_ID,
                                eventCategory=EVT_CATEG,
                                eventType=win32evtlog.EVENTLOG_INFORMATION_TYPE,
                                strings=EVT_STRS,
                                data=EVT_DATA)


# Output to log "log.txt" any open ports
def logger(ip_addr, port_num):
    n = datetime.now()
    with open('logs.txt', 'a') as file:
        file.write(f'{n} || {ip_addr}:{port_num} | OPEN \n')


# Create a socket and check if port is open closed after 0.3 seconds
def port_scan(network, port):
    for host in network:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((str(host), port))
        if result == 0:
            print(f" {host} Port: {port} : OPEN")
            logger(host, port)
            event_viewer((str(host)))
        else:
            print(f" {host} Port: {port} : CLOSED")


# Print the time it took for the program to execute.
def time_check(start, end):
    total = end - start
    return total


# Execute program
def main():
    # ip_net2 = list(ipaddress.IPv4Network(input('Enter an IP network address: ')))
    ip_net2 = list(ipaddress.IPv4Network('192.168.8.0/24'))
    ip_net = [ip for ip in ip_net2[10:] if int(ip) % 2 != 0]
    then = datetime.now()

    try:
        with open('port.txt') as file:
            port_num = int(file.read())
            print("Found", port_num, "in port.txt")
            print("Scanning")
            time.sleep(0.3)
            print("----------")

        if port_checker(port_num) is True:
            port_scan(ip_net, port_num)

        else:
            print("Enter a valid port between 0 - 65335")

    except:
        print("Error: port.txt not found")

    now = datetime.now()
    print(time_check(then, now))


main()
