#Partie 2

class Node:
    def __init__(self, value):
        """
        Value : valeur du noeud
        """
        self.value = value
        
    def __str__(self):
        """
        Retourne la valeur du noeud convertie en string
        """
        return str(self.value)

    def getValue(self):
        """
        Retourne la valeur du noeud
        """
        return self.value
            
    def setValue(self, v):
        """
        Modifie la valeur du noeud
        """
        self.value = v
        
class HyperNode(Node):
    def __init__(self, value):
        """
        hyperAretes : hyper-arêtes qui contiennent le noeud
        """
        super().__init__(value) #Pour initialiser la valeur du noeud
        self.hyperAretes = []
    
    def appendHyperArete(self, h):
        """
        Permet d'annoncer que le noeud appartient à l'hyper-arête h
        """
        if h not in self.hyperAretes:
            self.hyperAretes.append(h)
            
    def getHyperAretes(self):
        """
        Renvoie les hyperAretes auxquelles l'hyperNoeud appartient
        """
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
        """
        Renvoie le nom de l'hyperArete, suivi des noeuds qu'elle contient
        """
        return self.getName()+": "+str([str(i) for i in self.nodes])
    
    def getName(self):
        """
        Renvoie le nom de l'hyperArete
        """
        return self.name
    
    def getNodes(self):
        """
        Renvoie les noeuds contenus dans l'hyperArete, sous forme de liste de noeuds
        """
        return self.nodes

class HyperGraph:
    def __init__(self, name, nodes=[], hyperAretes=[]):
        self.name = name
        self.nodes = nodes
        self.hyperAretes = hyperAretes
		
    def __str__(self):
        """
        Renvoie le nom de l'hyperGraphe, suivi des hyperAretes qu'il contient (et des hyperNoeuds qu'il contient)
        """
        resultat = self.getName()+": \n"
        for i in self.hyperAretes:
            resultat += i.getName()+": "+str([str(p) for p in i.getNodes()])+"\n"
        for i in self.getNodes(): #Pour l'affichage des noeuds qui n'appartiendraient pas à une hyperArete
            resultat+=str(i)+" "
        resultat+="\n"
        return resultat

    def getName(self):
        """
        Renvoie le nom de l'hyperGraphe
        """
        return self.name

    def addHyperArete(self, h):
        """
        Rajoute une hyperArete si elle n'existe pas dans l'hyperGraphe
        """
        if h not in self.hyperAretes:
            self.hyperAretes.append(h)

    def addNode(self, n):
        """
        Ajoute un hyperNoeud si il n'existe pas dans l'hyperGraphe
        """
        if n not in self.nodes:
            self.nodes.append(n)
    
    def getHyperAretes(self):
        """
        Renvoie les hyperAretes de l'hyperGraphe, sous forme de liste
        """
        return self.hyperAretes
    
    def getNodes(self):
        """
        Renvoie les hyperNoeuds de l'hyperGraphe, sous forme de liste
        """
        return self.nodes

class Graph:
    """
    Cette classe désigne les graphe "simples", c'est-à-dire sans hyper-arêtes
    """
    def __init__(self):
        """
        Les noeuds du graphe sont stockés sous forme de dictionnaire où un noeud clé pointe vers des noeuds valeurs
        """
        self.nodes = {}
        
    def __str__(self):
        res = ""
        for k in self.nodes:
            res += str(k.getValue()) + ": "
            if self.nodes[k]:
                for i in self.nodes[k]:
                    res += str(i.getValue()) + " "
                res += "\n"
        return res

    def __eq__(self, other):
        """
        Deux graphe sont égaux si leurs noeuds (et donc, ici, leurs arêtes aussi), sont égaux
        """
        return self.nodes == other.nodes

    def size(self):
        """
        Renvoie la taille du graphe, son nombre de noeuds
        """
        return len(list(self.nodes.keys()))
    
    def appendNode(self, node, pointedNodes=0):
        """
        Ajoute un noeud au graphe, si il n'est pas déjà dedans
        """
        if node not in list(self.nodes.keys()) and pointedNodes==0:
            self.nodes[node] = []
        elif node not in self.nodes:
            self.nodes[node] = pointedNodes

    def delNode(self, node):
        """
        Supprime du graphe le noeud passé en paramètre (si il est dans le graphe)
        """
        if node in list(self.nodes.keys()):
            del self.nodes[node]
        
    def makePointNode(self, node, otherNode):
        """
        Indique qu'un noeud est directement accessible depuis un autre noeud
        """
        if node in self.nodes and otherNode not in self.nodes[node]:
            self.nodes[node].append(otherNode)

    def getNodes(self):
        """
        Renvoie le dictionnaire de noeuds
        """
        return self.nodes

    def getVoisins(self, n):
        """
        Renvoie la liste des voisins du noeud passé en paramètre
        """
        if n in list(self.nodes.keys()):
            return self.nodes[n]

def initH():
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

def initG():
    """
    Seconde fonction de test
    """
    a, b, c, d, e, f, g= HyperNode("v1"), HyperNode("v2"), HyperNode("v3"), HyperNode("v4"), HyperNode("v5"), HyperNode("v6"), HyperNode("v7")
    v = HyperArete("E1", [a, b, c])
    w = HyperArete("E2", [a, e])
    x = HyperArete("E3", [c, e, f])
    y = HyperArete("E4", [d])
    G = HyperGraph("G", [a, b, c, d, e, f, g], [v, w, x, y])
    return G

if __name__ == "__main__":
    H = initG()
    print(H)
