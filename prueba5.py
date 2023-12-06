from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

class RedTelematica(Topo):
    "Topología"
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

        # Switches con OpenFlow
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', protocols='OpenFlow13')
        s5 = self.addSwitch('s5', protocols='OpenFlow13')
        s6 = self.addSwitch('s6', protocols='OpenFlow13')

        # Conectar hosts a switches con OpenFlow
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h10, s3)
        self.addLink(h11, s3)
        self.addLink(h12, s4)
        self.addLink(h13, s4)

        # Conectar switches entre sí con OpenFlow
        self.addLink(s1, s2)
        self.addLink(s3, s4)
        self.addLink(s5, s6)

if __name__ == '__main__':
    topo = RedTelematica()
    net = Mininet(topo)
    net.start()

    print("Conexiones entre nodos:")
    dumpNodeConnections(net.hosts)

    # Ejecutar comandos, realizar pruebas, etc.

    net.stop()
