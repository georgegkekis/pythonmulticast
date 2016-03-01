import socket
import sys
import re

mac = '001723f14717'

def check_version(mydata):
    if len(mydata) != 2:
        return -1
    if mydata[0] == mac and mydata[1] == '*VERSION:2.4.0':
        return 1
    else:
        return -1

def check_loopdetection(mydata):
    if mydata[0] == mac and mydata[1] == '*LOOPDETECTION':
        return 1
    else:
        return -1

def check_status(mydata):
    if mydata[0] == mac and mydata[1] == '*STATUS':
        return 1
    else:
        return -1

def check_heartbeat(mydata):
    if len(mydata) != 2:
        return -1
    if mydata[0] == mac and mydata[1] == '*WB45HB':
        return 1
    else:
        return -1

def check_survey(mydata):
    surveylist =[]
    while mydata[0] == mac and mydata[1] == '*SITESURVEY': 
        print >>sys.stderr, 'received a valid survey:\nMAC address:%s\nSSID:%s' %(mydata[0],mydata[2])   
        surveylist.append(mydata)
        data, address = sock.recvfrom(1024)
        mydata = re.split(',',data)
    print >>sys.stderr, 'syrvey data:%s\n\n\n\n' % len(surveylist)
    print >>sys.stderr, 'syrvey data:%s\n%s' % (surveylist[0][0],surveylist[1][0])

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

    valid = -1
    #checking the data
    if mydata[1] == '*VERSION:2.4.0':
        valid = check_version(mydata)
    elif mydata[1] == '*LOOPDETECTION':
        valid = check_loopdetection(mydata)
    elif mydata[1] == '*STATUS':
        valid = check_status(mydata)
    elif mydata[1] == '*WB45HB':
        valid = check_heartbeat(mydata)
    elif mydata[1] == '*SITESURVEY':
        valid = check_survey(mydata)
    else:
        print 'data is not recognizable'

    if valid > 0: print 'data  valid'
    else: print 'data not valid'
    print >>sys.stderr, 'sending acknowledgement to', address
    sock.sendto('ack', address)

