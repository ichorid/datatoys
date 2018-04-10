from twisted.internet import protocol, reactor

class EchoProtocol(protocol.Protocol):
    def connectionMade(self):
        p = self.transport.getPeer()
        self.peer = '%s:%s' % (p.host, p.port)
        print "connected from", self.peer
    def dataReceived(self, data):
        self.transport.write(data)
    def connectionLost(self, reason):
        print "disconnected from %s:%s" % (self.peer, reason.value)

factory = protocol.Factory()
factory.protocol = EchoProtocol

reactor.listenTCP(8881, factory)
def hello(): print 'Listening on port', 8881
reactor.callWhenRunning(hello)
reactor.run()
