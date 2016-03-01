import socket
import sys
import re

mac = '001723f14717'

def check_version(mac, mydata):
    if len(mydata) != 2:
        return -1
    if mydata[0] == mac :
        return 1
    else:
        return -1

def check_loopdetection(mac, mydata):
    if mydata[0] == mac :
        return 1
    else:
        return -1

def check_status(mac, mydata):
    if mydata[0] == mac :
        return 1
    else:
        return -1

def check_heartbeat(mac, mydata):
    if len(mydata) != 2:
        return -1
    if mydata[0] == mac :
        return 1
    else:
        return -1

def check_survey(mac, mydata):
    surveylist =[]
    if mydata[0] == mac : 
        return 1
    else:
        return -1

def receiverinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 50000))
    return sock

sock = receiverinit()
# Receive/respond loop
while True:
    mydata = []
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)

    #parsing the data
    mydata = re.split(',',data)
    print 'mydata == %s' %mydata
    if len(mydata) < 2:
        print 'not enough arguments'
        valid = -1
    else:
        valid = -1
        #checking the data
        if mydata[1][:9] == '*VERSION:':
            valid = check_version(mac, mydata)
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

    if valid > 0: print 'data valid'
    else: print 'data not valid'

