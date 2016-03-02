import socket
import sys
import re

mac = '001723f14717'
version  = '2.4.0'
loopnu = [None, None, None ]
ssid = 'dimitris2'

def check_version(mydata, version):
    if len(mydata) != 2:
        return False
    return version == mydata[1][9:]

def check_loopdetection(mydata):
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
    return True

def check_status(mydata):
    if len(mydata) != 4:
        return False
    try:
        val = int(mydata[3])
    except ValueError:
        return False
    return (-30 > val > -100)

def check_heartbeat(mydata):
    if len(mydata) != 2:
        return False
    return True

def parse_survey(surveys, mydata):
    if len(mydata) != 5:
        return False
    try:
        val = int(mydata[3])
    except ValueError:
        return False
    surveys.append(mydata)
    return False


def check_survey(surveys, ssid):
    for s in surveys:
        if s[2] == ssid: return True
    return False

def receiverinit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 50000))
    return sock

def check_mac(mac, mydata):
    return mydata[0] == mac

sock = receiverinit()
# Receive/respond loop
insurvey = False
surveys = []
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)

    #parsing the data
    mydata = re.split(',',data)
    print 'mydata == %s' %mydata
    mac_ok = check_mac(mac, mydata)
    if mac_ok:
        print'mac is ok'
    else: 
        print 'mac not right\n'
        break
    if len(mydata) < 2:
        print 'not enough arguments'
        valid = False
    else:
        if mydata[1] == '*SITESURVEY':
            insurvey = True
            parse_survey(surveys, mydata)
            continue
        if insurvey:
            validsurvey = check_survey(surveys, ssid)
            if validsurvey:
                print '\n\nfound a valid survey!!!!!!!!(this is about previous packages sent so dont get confused ;-)\n\n'
            else:
                print '\n\nthe survey packets seem to be over and i didnt find a valid survey sorry ;-)\n\n'
            insurvey = False

        #checking the data
        if mydata[1][:9] == '*VERSION:':
            valid = check_version(mydata, version)
        elif mydata[1] == '*LOOPDETECTION':
            valid = check_loopdetection(mydata)
        elif mydata[1] == '*STATUS':
            valid = check_status(mydata)
        elif mydata[1] == '*WB45HB':
            valid = check_heartbeat(mydata)
        else:
            print 'data is not recognizable'
            valid = False

    if valid is True : print 'data valid'
    else: print 'data not valid'

