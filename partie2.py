#Partie 2

<<<<<<< HEAD
class hypergraphe(Object) :
=======
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
        return self.name
    
    def getNodes(self):
        return self.nodes

class HyperGraph:
    def __init__(self, name, nodes, hyperAretes):
        self.name = name
        self.nodes = nodes
        self.hyperAretes = hyperAretes
		
    def __str__(self):
    	return self.name
    
    def getHyperAretes(self):
        return self.hyperAretes
    
    def getNodes(self):
        return self.nodes

class Graph:
    """
    Cette classe désigne les graphe "simples", c'est-à-dire sans hyper-arêtes
    """
    def __init__(self):
        self.nodes = {}
    def __str__(self):
        res = ""
        for k in self.nodes:
            res += str(k) + ": "
            for i in self.nodes[k]:
                res += str(i) + " "
            res += "\n"
        return res
    
    def appendNode(self, node):
        if node not in self.nodes:
            self.nodes[node] = []
            
    def makePointNode(self, node, otherNode):
        if node in self.nodes:
            self.nodes[node].append(otherNode)

def initG():
    """
    Fonction de test qui crée un hyper-graphe
    """
    a, b, c, d = HyperNode(1), HyperNode(2), HyperNode(3), HyperNode(4)
    k = HyperArete("k", [a, b, c])
    l = HyperArete("l", [b, c, d])
    H = HyperGraph("H", [a,b,c,d],[k,l])
    return H

if __name__ == "__main__":
<<<<<<< HEAD
    H = initG()
=======
	a, b, c, d = Node(1), Node(2), Node(3), Node(4)
	k = HyperArete(a, b, c)
	l = HyperArete(b, c, d)
	H = HyperGraph([a,b,c,d],[k,l])
	print(H)
>>>>>>> 65ce700342e82d9ad29edc4212fb10b95d7b1dcc
>>>>>>> 9d123bdfd6e911bd1ccb98493f441dac7d8128d1
