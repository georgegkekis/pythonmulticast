import socket
import sys
import re

mac = '001723f14717'
version  = '2.4.0'
loopnu = [None, None, None ]

def check_version(mac, mydata, version):
    if len(mydata) != 2:
        return False
    return mydata[0] == mac and version == mydata[1][9:]

def check_loopdetection(mac, mydata):
    global loopnu
    val = []
    if len(mydata) != 5:
        return False
    try:
        val.append(int(mydata[2]))
        val.append(int(mydata[3]))
        val.append(int(mydata[4]))
    except ValueError:
        return False
    if loopnu[0] != None:
        print 'here are val==%s' % val
        if loopnu[0] != val[0] or loopnu[1] >= val[1] or loopnu[2] >= val[2]: return False
    loopnu = val
    return mydata[0] == mac

def check_status(mac, mydata):
    if len(mydata) != 4:
        return False
    try:
        val = int(mydata[3])
    except ValueError:
        return False
    return mydata[0] == mac and (-30 > val > -100)

def check_heartbeat(mac, mydata):
    if len(mydata) != 2:
        return False
    return mydata[0] == mac

def check_survey(mac, mydata):
    return mydata[0] == mac

def receiverinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 50000))
    return sock

sock = receiverinit()
# Receive/respond loop
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)

    #parsing the data
    mydata = re.split(',',data)
    print 'mydata == %s' %mydata
    if len(mydata) < 2:
        print 'not enough arguments'
        valid = False
    else:
        #checking the data
        if mydata[1][:9] == '*VERSION:':
            valid = check_version(mac, mydata, version)
        elif mydata[1] == '*LOOPDETECTION':
            valid = check_loopdetection(mac, mydata)
        elif mydata[1] == '*STATUS':
            valid = check_status(mac, mydata)
        elif mydata[1] == '*WB45HB':
            valid = check_heartbeat(mac, mydata)
        elif mydata[1] == '*SITESURVEY':
            valid = check_survey(mac, mydata)
        else:
            print 'data is not recognizable'
            valid = False

    if valid is True : print 'data valid'
    else: print 'data not valid'

