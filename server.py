#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class Server(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.quote + '\r\n')
    def connectionLost(self, reason):
        ip, port = self.transport.client
        #print str(self.transport.getPeer()) + ': connection lost'
        print 'Client ' + str(ip) + ':' + str(port) + ': connection lost'
    def dataReceived(self, data):
        print data
        self.transport.write(data)

class ServerFactory(Factory):
    protocol = Server
    def __init__(self, quote=None):
        self.quote = quote

reactor.listenTCP(8007, ServerFactory("Connection with server has been extablished."))
reactor.run()