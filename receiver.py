import socket
import struct
import sys
import re

def check_heartbeat(mydata):
     #check that the list has only two elements
    if len(mydata) != 2:
        return -1

    #check that data[1] == '*WB45HB'
    if mydata[0] == '001723f14717' and mydata[1] == '*WB45HB':
        print >>sys.stderr, 'received a valid heart beat:\nMAC address:%s\nidentity:%s' %(mydata[0],mydata[1])
        return 1
    else:
        print >>sys.stderr, 'this is not a valid heart beat will continue with other checks'
        return -1
    #FIXME:handle exceptions
    

multicast_group = '127.0.0.1'
server_address = ('', 50000)
command = 'somecommand'

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)


# Receive/respond loop
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data

    #parsing the data
    mydata = re.split(',',data)
    found = check_heartbeat(mydata)
    print >>sys.stderr,found
    print >>sys.stderr, '\nsending acknowledgement to', address
    sock.sendto('ack', address)
    
    sent = sock.sendto(command, address)



'''def check_loopdetection(mydata):
    #checks for valid lopdetection messages

def check_status(mydata):
    #checks for valid status

def check_survey(mydata):
    #checks for valid survey'''
