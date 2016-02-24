import socket
import struct
import time
import sys

msgheartbeat = '001723f14717,*WB45HB'
msgloopdetection = '001723F14717,*LOOPDETECTION,3523115984,851,853'
msgversion = '001723f14717,*VERSION:2.4.0'
msgstatus = '001723f14717,*STATUS,Authenticated,-73'
msgsitesyrvey = '001723f14717,*SITESURVEY,tswpa,-68,WPA2-PSK-AES\n001723f14717,*SITESURVEY,dimitris2,-76,WPA2-PSK-AES\n001723f14717,*SITESURVEY,dimitris-public,-75,WPA2-PSK-AES\n001723f14717,*SITESURVEY,dimitris2,-66,WPA2-PSK-AES\n001723f14717,*SITESURVEY,dimitris-public,-66,WPA2-PSK-AES'

multicast_group = ('127.0.0.1', 50000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(11.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

while 1:
    # Send data to the multicast group
    print >>sys.stderr, 'sending "%s"' % msgsitesyrvey
    sent = sock.sendto(msgsitesyrvey, multicast_group)
    time.sleep(1)
    

