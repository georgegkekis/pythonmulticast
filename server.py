import socket
import struct
import time
import sys

def serverinit():

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(11.2)

    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    return sock

def sendversion(mac , version):
    print >>sys.stderr, 'sending version\n'
    sent = sock.sendto(mac + ',*VERSION'+ version, multicast_group)

def sendloopdetection(mac , nu1 , nu2 ,nu3):
    print >>sys.stderr, 'sending loopdetection\n'
    sent = sock.sendto(mac + ',*LOOPDETECTION'+ nu1 + nu2 + nu3 , multicast_group)
    
def sendstatus(mac , status , signalst):
    print >>sys.stderr, 'sending status\n'
    sent = sock.sendto(mac + ',*status'+ status + signalst , multicast_group)

'''def sendheartbeat(mac , identification):

def sendsurvey(mac , ssid , signalst , secur):'''

msgheartbeat = '001723f14717,*WB45HB'
msgloopdetection = '001723F14717,*LOOPDETECTION,3523115984,851,853'
msgversion = '001723f14717,*VERSION:2.4.0'
msgstatus = '001723f14717,*STATUS,Authenticated,-73'
msgsitesyrvey1 = '001723f14717,*SITESURVEY,tswpa,-68,WPA2-PSK-AES' 
msgsitesyrvey2 = '001723f14717,*SITESURVEY,dimitris2,-76,WPA2-PSK-AES' 
msgsitesyrvey3 = '001723f14717,*SITESURVEY,dimitris-public,-75,WPA2-PSK-AES'
msgsitesyrvey4 = '001723f14717,*SITESURVEY,dimitris2,-66,WPA2-PSK-AES'
msgsitesyrvey5 = '001723f14717,*SITESURVEY,dimitris-public,-66,WPA2-PSK-AES'

multicast_group = ('127.0.0.1', 50000)
sock = serverinit()
sendversion('001723f14717' , ':2.4.0')
sendloopdetection('001723f14717' , ',3523115984' , ',851' ,',853')  
sendstatus('001723f14717' , ',Authenticated' , ',-73')  


