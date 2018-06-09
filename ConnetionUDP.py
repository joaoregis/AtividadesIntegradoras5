import socket

class ConnetionUDP:
    __UDP_PORT__ = 555
    __ADDR_LIST__ = []

    def __init__(self, port):
        self.__UDP_PORT__ = port
        self.sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
        self.sock.bind(('', self.__UDP_PORT__))
        self.__ADDR_LIST__ = set([])

    def SendData(self, data, iptarget):
        self.sock.sendto(str(int(data)).encode(), iptarget)
        
    def ReciveData(self):
        data, addr = self.sock.recvfrom(255)
        self.__ADDR_LIST__.add(addr)
        return (str(data.decode()), addr)
    
    def GetAddrList(self):
        return self.__ADDR_LIST__


