#!/usr/bin/env python
 
LISTEN_PORT = 8000
SERVER_PORT = 1234
SERVER_ADDR = "10.0.3.3"
HEADER = "ffffffff"
PAYLOAD = "abcd"*600
DATA = (HEADER + PAYLOAD).decode("HEX")
 
from twisted.internet import protocol, reactor
 
 
class ServerProtocol(protocol.DatagramProtocol):
    def startProtocol(self):
        while (True):
            self.transport.write(DATA, (SERVER_ADDR, SERVER_PORT))


    def datagramReceived(self, data, (host, port)):
        pass
 
def main():
    sp = ServerProtocol();
    reactor.listenUDP(LISTEN_PORT, sp)
    reactor.run()
 
 
if __name__ == '__main__':
    main()
