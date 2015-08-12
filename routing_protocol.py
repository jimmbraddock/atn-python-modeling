# -*- coding: koi8-r -*-
import threading
import scheduler

MSG_ERROR = 1
MSG_REQUEST = 2
MSG_REPLY = 3
MSG_HELLO = 4
timer = scheduler.timerSingleton()


class RoutingEntry:
    def __init__(self, next_node, hop_count):
        self.next_node = next_node
        self.hop_count = hop_count


class RoutingTable:
    def __init__(self):
        self.entries = {}


class RoutingProtocol:
    def __init__(self, node):
        self.routing_table = RoutingTable()
        self.node = node

    def send(self, receiver, packet):
        GlobalRouter.routing_protocols[receiver].recv(self.node, packet)

    def send_hello(self):
        print('[' + str(self.node.id) + '] Отправляем Hello')
        for n in GlobalRouter.nodes:
            if n != self.node and self.node.range > self.node.get_path_len(n):
                packet = Packet(sender=self.node, reciever=n,
                                msg_type=MSG_HELLO, load=self.routing_table)
                self.send(n, packet)

        timer.scheduler(2, self.send_hello)

    def recv(self, sender, packet):
        if packet.msg_type == MSG_HELLO:
            self.recv_hello(packet)

    def recv_hello(self, packet):
        rt = packet.load
        for entry in list(rt.entries.keys()) + [packet.sender]:
            if entry not in list(self.routing_table.entries.keys()) and \
                            entry != self.node:
                if entry == packet.sender:
                    hop_count = 1
                else:
                    hop_count = rt.entries[entry].hop_count + 1
                self.routing_table.entries[entry] = RoutingEntry(packet.sender,
                                                                 hop_count)
        print('[' + str(self.node.id) + '] Таблица: ')
        for k in self.routing_table.entries.keys():
            print('   ' + str(k.id))

    def recv_error(self):
        pass

    def recv_reply(self):
        pass

    def recv_request(self, sender):
        pass

    def forward_packet(self):
        pass


class GlobalRouter:
    nodes = []
    routing_protocols = {}

    def __init__(self, nodes):
        for n in nodes:
            GlobalRouter.routing_protocols[n] = RoutingProtocol(n)
        GlobalRouter.nodes = nodes
        self.run()

    def run(self):
        for r in GlobalRouter.routing_protocols.values():
            t = threading.Thread(target=r.send_hello)
            t.start()


class Packet:
    def __init__(self, sender=None, reciever=None, msg_type=None, load=None):
        self.sender = sender
        self.reciever = reciever
        self.msg_type = msg_type
        self.pos = sender.pos
        self.speed = sender.speed
        self.load = load
