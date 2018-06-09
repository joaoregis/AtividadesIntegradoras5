import sys
from ConnetionUDP import ConnetionUDP
from LDR import LDR
from LED import LED
from USC import UniversalCoverter
from OrderScale import OrderScale
import socket


address = "192.168.43.107"

myled = LED()

myldr = LDR()

rbscale = UniversalCoverter(100,10,OrderScale.DESCENDING)

nmcuscale = UniversalCoverter(0,100, OrderScale.ASCENDING)


sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
sock.bind((address, 555))

while True:
    
    print('Waiting to receive anything ...')
    data, addr = sock.recvfrom(1024)
    
    #data, addr = conn.ReciveData()

    if data.decode() != '':
        print ('Raw data ::: ', data)
        nodeldrvalue = nmcuscale.GetValueUniversalScale(float(data.decode()))
        print ('NodeMCU Value ::: ',  nodeldrvalue, '\n')

    raspberryldrvalue = nmcuscale.GetValueUniversalScale(myldr.GetLDRCount())
    
    print ('Rasperry Value ::: ',  raspberryldrvalue, '\n')
    
    if (abs( nodeldrvalue - raspberryldrvalue ) < 4):
        sock.sendto('2'.encode(), addr)
        #conn.SendData(2, addr)
        myled.sendsignalled("blink")
        
    elif (nodeldrvalue > raspberryldrvalue):
        sock.sendto('0'.encode(), addr)
        #conn.SendData(0, addr)
        myled.sendsignalled("off")

    elif (nodeldrvalue < raspberryldrvalue):
        sock.sendto('1'.encode(), addr)
        #conn.SendData(1, addr)
        myled.sendsignalled("on")
