#Partie 2

class Node:
    def __init__(self, value):
        """
        Value : valeur du noeud
        """
        self.value = value
        
    def __str__(self):
        return str(self.value)
            
    def getValue(self):
        return self.value
            
    def setValue(self, v):
        self.value = v
        
class HyperNode(Node):
    def __init__(self, value):
        """
        hyperAretes : hyper-arêtes qui contiennent le noeud
        """
        super().__init__(value)
        self.hyperAretes = []
            
    def appendHyperArete(self, h):
        """
        Permet d'annoncer que le noeud appartient à l'hyper-arête h
        """
        if h not in self.hyperAretes:
            self.hyperAretes.append(h)
            
    def getHyperAretes(self):
        return self.hyperAretes
	
class HyperArete:
    def __init__(self, name, nodes):
        """
        nodes : les noeuds qui sont contenus dans l'hyper-arête
        Ceux-ci sont modifiés pour indiquer qu'ils soient contenus dans l'hyper-arête
        """
        self.name = name
        self.nodes = nodes
        for i in self.nodes:
            i.appendHyperArete(self)
            
    def __str__(self):
        return self.getName()+": "+str([str(i) for i in self.nodes])

    def getName(self):
        return self.name
    
    def getNodes(self):
        return self.nodes

class HyperGraph:
    def __init__(self, name, nodes, hyperAretes):
        self.name = name
        self.nodes = nodes
        self.hyperAretes = hyperAretes
		
    def __str__(self):
        resultat = self.getName()+": \n"
        for i in self.hyperAretes:
            resultat += i.getName()+": "+str([str(p) for p in i.getNodes()])+"\n"
        return resultat

    def getName(self):
        return self.name

    def addHyperArete(self, h):
        if h not in self.hyperAretes:
            self.hyperAretes.append(h)

    def addNode(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
    
    def getHyperAretes(self):
        return self.hyperAretes
    
    def getNodes(self):
        return self.nodes

class Graph:
    """
    Cette classe désigne les graphe "simples", c'est-à-dire sans hyper-arêtes
    """
    def __init__(self):
        self.nodes  = {}
        
    def __str__(self):
        res = ""
        for k in self.nodes:
            res += str(k.getValue()) + ": "
            for i in self.nodes[k]:
                res += str(i.getValue()) + " "
            res += "\n"
        return res
    
    def appendNode(self, node):
        if node not in self.nodes:
            self.nodes[node] = []
            
    def makePointNode(self, node, otherNode):
        if node in self.nodes and otherNode not in self.nodes[node]:
            self.nodes[node].append(otherNode)

def initG():
    """
    Fonction de test qui crée un hyper-graphe
    """
    a, b, c, d, e, f, g, h, i= HyperNode("v1"), HyperNode("v2"), HyperNode("v3"), HyperNode("v4"), HyperNode("v5"), HyperNode("v6"), HyperNode("v7"), HyperNode("v8"), HyperNode("v9")
    v = HyperArete("E1", [a, b, d])
    w = HyperArete("E2", [c, e, f, h])
    x = HyperArete("E3", [d, e, f])
    y = HyperArete("E4", [e, f, h, i])
    z = HyperArete("E5", [i])
    H = HyperGraph("H", [a, b, c, d, e, f, g, h, i],[v, w, x, y, z])
    return H

if __name__ == "__main__":
    H = initG()
