import socket
import struct
import time
import sys

multicast_group = ('127.0.0.1', 50000)
mac = '001723f14717'

def sendversion(mac, version, verbose=True):
    if verbose: print >>sys.stderr, 'sending version\n'
    sent = sock.sendto(mac + ',*VERSION:'+ version, multicast_group)

def sendloopdetection(mac, nu1 , nu2 ,nu3, verbose=True):
    if verbose: print >>sys.stderr, 'sending loopdetection\n'
    sent = sock.sendto(mac + ',*LOOPDETECTION,'+ nu1 + ',' + nu2 + ',' + nu3, multicast_group)
    
def sendstatus(mac, status, signalst, verbose=True):
    if verbose: print >>sys.stderr, 'sending status\n'
    sent = sock.sendto(mac + ',*STATUS,'+ status +',' + signalst , multicast_group)

def sendheartbeat(mac, verbose=True):
    if verbose: print >>sys.stderr, 'sending heartbeat\n'
    sent = sock.sendto(mac + ',*WB45HB' , multicast_group)

def sendsurvey(mac , ssid , signalst , secur, verbose=True):
    if verbose: print >>sys.stderr, 'sending survey\n'
    sent = sock.sendto(mac + ',*SITESURVEY,' + ssid + ',' + signalst + ',' + secur, multicast_group)




sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendversion(mac, '2.4.0')
sendloopdetection(mac, '3523115984' , '851' ,'853')  
sendstatus(mac, 'Authenticated' , '-73')  
sendheartbeat(mac)
sendsurvey(mac, 'tswpa' , '-68' , 'WPA2-PSK-AES')


