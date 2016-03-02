import socket
import struct
import time
import sys

mac = '001723f14717'

def serverinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('127.0.0.1', 50000))
    return sock

def sendversion(sock, mac, version, verbose=True):
    if verbose: print >>sys.stderr, 'sending version\n'
    sent = sock.send(mac + ',*VERSION:'+ version)

def sendloopdetection(sock, mac, nu1 , nu2 ,nu3, verbose=True):
    if verbose: print >>sys.stderr, 'sending loopdetection\n'
    sent = sock.send(mac + ',*LOOPDETECTION,'+ nu1 + ',' + nu2 + ',' + nu3)
    
def sendstatus(sock, mac, status, signalst, verbose=True):
    if verbose: print >>sys.stderr, 'sending status\n'
    sent = sock.send(mac + ',*STATUS,'+ status +',' + signalst)

def sendheartbeat(sock, mac, verbose=True):
    if verbose: print >>sys.stderr, 'sending heartbeat\n'
    sent = sock.send(mac + ',*WB45HB')

def sendsurvey(sock, mac , ssid , signalst , secur, verbose=True):
    if verbose: print >>sys.stderr, 'sending survey\n'
    sent = sock.send(mac + ',*SITESURVEY,' + ssid + ',' + signalst + ',' + secur)

def sendinvalidstring(sock, verbose=True):
    if verbose: print >>sys.stderr, 'sending invalid string\n'
    sent = sock.send('hgdfsdfsfss,*WB45HB,sgdsgherhdh,egtergesrg,,,,')



sock = serverinit()
sendversion(sock, mac, '2.4.0')
sendloopdetection(sock, mac, '3523115984' , '851' ,'853')  
sendstatus(sock, mac, 'Authenticated' , '-73')  
sendheartbeat(sock, mac)
sendsurvey(sock, mac, 'tswpa' , '-68' , 'WPA2-PSK-AES')
#sendsurvey(sock, mac, 'dimitris2' , '-76' , 'WPA2-PSK-AES')
sendsurvey(sock, mac, 'dimitris-public' , '-75' , 'WPA2-PSK-AES')
sendsurvey(sock, mac, 'dimitris-public' , '-68' , 'WPA2-PSK-AES')
sendinvalidstring(sock)
sendheartbeat(sock, mac)
sendinvalidstring(sock)
sendheartbeat(sock, mac)
sendinvalidstring(sock)
sendheartbeat(sock, mac)
sendinvalidstring(sock)
sendheartbeat(sock, mac)

