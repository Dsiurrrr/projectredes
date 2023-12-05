#POR EDITAR
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

class RedTelematica(Topo):
    "Topologia"
    def build(self):
        # host Red Campus
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        # host Red Telematica
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        # host Sede Central
        h10 = self.addHost('h10')
        # switch Core
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        # switch nodos distribucion
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s41 = self.addSwitch('s41')
        s42 = self.addSwitch('s42')
        s43 = self.addSwitch('s43')
        s44 = self.addSwitch('s44')
        # switch acceso
        # switch nodo1
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')
        s19 = self.addSwitch('s19')
        s8 = self.addSwitch('s8')
        # switch nodo2
        s24 = self.addSwitch('s24')
        s25 = self.addSwitch('s25')
        s26 = self.addSwitch('s26')
        s9 = self.addSwitch('s9')
        # switch nodo3
        s27 = self.addSwitch('s27')
        s28 = self.addSwitch('s28')
        s29 = self.addSwitch('s29')
        s10 = self.addSwitch('s10')
        # switch nodo4
        s30 = self.addSwitch('s30')
        s31 = self.addSwitch('s31')
        s32 = self.addSwitch('s32')
        s33 = self.addSwitch('s33')
        s11 = self.addSwitch('s11')
        # switch nodo5
        s12 = self.addSwitch('s12')
        # switch nodo6
        s13 = self.addSwitch('s13')
        # switch nodo7
        s14 = self.addSwitch('s14')
        # switch nodo8
        s34 = self.addSwitch('s34')
        s35 = self.addSwitch('s35')
        s36 = self.addSwitch('s36')
        s37 = self.addSwitch('s37')
        s15 = self.addSwitch('s15')
        # switch nodo9
        s38 = self.addSwitch('s38')
        s39 = self.addSwitch('s39')
        s40 = self.addSwitch('s40')
        s16 = self.addSwitch('s16')
        # switch Red Telematica
        s20 = self.addSwitch('s20')
        s21 = self.addSwitch('s21')
        s22 = self.addSwitch('s22')
        # switch sede central
        s23 = self.addSwitch('s23')
        # links entre cores
        self.addLink(s1, s2)
        # links distribucion a core1
        self.addLink(s3, s1)
        self.addLink(s4, s1)
        self.addLink(s5, s1)
        self.addLink(s6, s1)
        self.addLink(s7, s1)
        self.addLink(s41, s1)
        # links distribucion a core2
        self.addLink(s42, s2)
        self.addLink(s43, s2)
        self.addLink(s44, s2)
        # link acceso
        # link nodo1
        self.addLink(s17, s3)
        self.addLink(s18, s3)
        self.addLink(s19, s3)
        self.addLink(s8, s3)
        # link nodo2
        self.addLink(s24, s4)
        self.addLink(s25, s4)
        self.addLink(s26, s4)
        self.addLink(s9, s4)
        # link nodo3
        self.addLink(s27, s5)
        self.addLink(s28, s5)
        self.addLink(s29, s5)
        self.addLink(s10, s5)
        # link nodo4
        self.addLink(s30, s6)
        self.addLink(s31, s6)
        self.addLink(s32, s6)
        self.addLink(s33, s6)
        self.addLink(s11, s6)
        # link nodo5
        self.addLink(s12, s7)
        # link nodo6
        self.addLink(s13, s41)
        # link nodo7
        self.addLink(s14, s42)
        # link nodo8
        self.addLink(s34, s43)
        self.addLink(s35, s43)
        self.addLink(s36, s43)
        self.addLink(s37, s43)
        self.addLink(s15, s43)
        # link nodo9
        self.addLink(s38, s44)
        self.addLink(s39, s44)
        self.addLink(s40, s44)
        self.addLink(s16, s44)
        # link Red Telematica
        self.addLink(s20, s1)
        self.addLink(s21, s1)
        self.addLink(s22, s1)
        # link Sede Central
        self.addLink(s23, s2)
        # link host acceso
        self.addLink(h1, s8)
        self.addLink(h2, s9)
        self.addLink(h3, s10)
        self.addLink(h4, s11)
        self.addLink(h5, s12)
        self.addLink(h6, s13)
        self.addLink(h7, s14)
        self.addLink(h8, s15)
        self.addLink(h9, s16)
        # Links host Red Telematica
        self.addLink(s20, h11)
        self.addLink(s21, h12)
        self.addLink(s22, h13)
        # Links host Sede Central
        self.addLink(s23, h10)
        
# Permite al archivo ser importado con `mn --custom <filename> --topo minimal`
topos = {
'RedTelematica': RedTelematica
}
