import sys
from LDR import LDR
from LED import LED
from USC import UniversalCoverter
from OrderScale import OrderScale
import socket


address = "192.168.43.161"

myled = LED()

myldr = LDR()

rbscale = UniversalCoverter(100,10,OrderScale.DESCENDING)

nmcuscale = UniversalCoverter(0,100, OrderScale.ASCENDING)

sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
sock.bind((address, 555))

while True:
    
    print('Waiting to receive anything ...')
    data, addr = sock.recvfrom(1024)

    if data.decode() != '':
        print ('NodeMCU Value ::: ', data)
        nodeldrvalue = nmcuscale.GetValueUniversalScale(float(data.decode()))

    raspberryldrvalue = nmcuscale.GetValueUniversalScale(myldr.GetLDRCount())
    
    print ('Rasperry Value ::: ',  raspberryldrvalue, '\n')
    
    if (abs( nodeldrvalue - raspberryldrvalue ) < 8):
        sock.sendto('2'.encode(), addr)
        myled.sendsignalled("blink")
        
    elif (nodeldrvalue > raspberryldrvalue):
        sock.sendto('0'.encode(), addr)
        myled.sendsignalled("off")

    elif (nodeldrvalue < raspberryldrvalue):
        sock.sendto('1'.encode(), addr)
        myled.sendsignalled("on")
