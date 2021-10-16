#!/usr/bin/python2
import socket
import sys
import time

found_users = []

if len(sys.argv) != 3:
    print("Usage: smtp_enumerate.py <target_ip> <username_list>")
    sys.exit(0)
    
# Read the username list
username_list = open(sys.argv[2], "r")

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
print(sys.argv[1])
connect = s.connect((sys.argv[1], 25))

# Receive the banner
banner = s.recv(1024)
print(banner)

# SEND HELO msg if just in case
s.send("HELO hi\r\n")
s.recv(1024)

# VRFY a list of users
for user in username_list:
    user = user.rstrip()
    print("Trying user: " + user)
    s.send('VRFY ' + user + '\r\n')
    result = s.recv(1024)
    if "unknown" not in result:
        found_users.append(user)
        print("User found: " + user)

# Print found users
print("")
print("Users found:")
for user in found_users:
    print("Found user: " + user.rstrip())

# Close the socket
s.close()
