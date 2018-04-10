#!/usr/bin/env python
 
LISTEN_PORT = 8000
SERVER_PORT = 1234
SERVER_ADDR = "10.0.3.3"
 
from twisted.internet import protocol, reactor
 
 
class ServerProtocol(protocol.DatagramProtocol):
    def datagramReceived(self, data, (host, port)):
        #print "received %r from %s:%d" %  (data, host, port)
        self.transport.write(data, (SERVER_ADDR, SERVER_PORT))
 
 
 
def main():

    sp = ServerProtocol();
    reactor.listenUDP(LISTEN_PORT, sp)
    reactor.run()
 
 
if __name__ == '__main__':
    main()
