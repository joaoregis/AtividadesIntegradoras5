import sys
from ConnetionUDP import ConnetionUDP
from LDR import LDR
from LED import LED
from USC import UniversalCoverter
from OrderScale import OrderScale


ddress = "192.168.43.107"

myled = LED()

myldr = LDR()

rbscale = UniversalCoverter(100,10,OrderScale.DESCENDING)

nmcuscale = UniversalCoverter(0,100, OrderScale.ASCENDING)

conn = ConnetionUDP(555)

while True:
    
    data, addr = conn.ReciveData()

    if data != '':
        nodeldrvalue = nmcuscale.GetValueUniversalScale(float(data))
    else:
        nodeldrvalue = nmcuscale.GetValueUniversalScale(float(0))

    raspberryldrvalue = nmcuscale.GetValueUniversalScale(myldr.GetLDRCount())
    
    print ('Node Value ',  nodeldrvalue, '\n')
    print ('Rasp Value ',  raspberryldrvalue, '\n')
    
    if (abs( nodeldrvalue - raspberryldrvalue ) < 4):
        conn.SendData(2, addr)
        myled.sendsignalled("blink")
        
    elif (nodeldrvalue > raspberryldrvalue):
        conn.SendData(0, addr)
        myled.sendsignalled("off")

    elif (nodeldrvalue < raspberryldrvalue):
        conn.SendData(1, addr)
        myled.sendsignalled("on")
