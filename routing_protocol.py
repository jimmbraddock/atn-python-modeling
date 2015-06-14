# -*- coding: koi8-r -*-

class RoutingEntry:
    def __init__(self, dest, next_node, hop_count):
        self.dest = dest
        self.next_node = next_node
        self.hop_count = hop_count

class RoutingTable:
    def __init__(self):
        self.entries = []

class RoutingProtocol:
    def __init__(self):
        self.routing_table = RoutingTable()


    def send(self, receiver):
        pass

    def send_hello(self):
        pass

    def recv(self, sender):
        pass

    def recv_error(self, sender):
        pass

    def recv_reply(self, sender):
        pass

    def recv_request(self, sender):
        pass

    def forward_packet(self):
        pass
