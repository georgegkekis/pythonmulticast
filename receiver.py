import socket
import struct
import sys
import re

multicast_group = '127.0.0.1'
server_address = ('', 50000)

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
    mydata = re.split(',|\n',data)
    '''print >>sys.stderr, '\ndata broken up to :\ndata1: %s\ndata2: %s\ndata3: %s\ndata4: %s\ndata5: %s\ndata6: %s\ndata7: %s\ndata8: %s' %(mydata[0],mydata[1],mydata[2],mydata[3],mydata[4],mydata[5],mydata[6],mydata[7])'''
    print >>sys.stderr,mydata
    print >>sys.stderr, 'sending acknowledgement to', address
    sock.sendto('ack', address)
