
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

class RedTelematica(Topo):
    "Topologia"
    def build(self):
        # Hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')

        # Switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s17 = self.addSwitch('s17')
        s24 = self.addSwitch('s24')
        s27 = self.addSwitch('s27')
        s28 = self.addSwitch('s28')
        s29 = self.addSwitch('s29')
        s30 = self.addSwitch('s30')
        s31 = self.addSwitch('s31')
        s32 = self.addSwitch('s32')
        s20 = self.addSwitch('s20')
        s21 = self.addSwitch('s21')
        s22 = self.addSwitch('s22')
        s23 = self.addSwitch('s23')

        # Links entre cores
        self.addLink(s1, s2)

        # Links distribucion a core1
        self.addLink(s3, s1)
        self.addLink(s4, s1)
        # Links distribucion a core2
        self.addLink(s5, s2)
        self.addLink(s6, s2)

        # Links acceso
        self.addLink(s17, s3)
        self.addLink(s24, s4)
        self.addLink(s27, s5)
        self.addLink(s28, s5)
        self.addLink(s29, s5)
        self.addLink(s30, s6)
        self.addLink(s31, s6)
        self.addLink(s32, s6)

        # Links Red Telematica
        self.addLink(s20, s1)
        self.addLink(s21, s1)
        self.addLink(s22, s1)
        # Links Sede Central
        self.addLink(s23, s2)

        # Links host acceso
        self.addLink(h1, s17)
        self.addLink(h2, s24)
        self.addLink(h3, s29)
        self.addLink(h4, s32)
        # Links host Red Telematica
        self.addLink(h11, s20)
        self.addLink(h12, s21)
        self.addLink(h13, s22)
        # Links host Sede Central
        self.addLink(h10, s23)

topos={"RedTelematica": RedTelematica}
