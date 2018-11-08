from partie2 import *

#Fichier qui gère les fonctions, on liera tout plus tard mais comme ça c'est plus clair.


def incidenceGraph(graph):
    """
    Cette fonction renvoie le graphe d'incidence
    """
    incidenceG = Graph()
    for h in graph.getHyperAretes(): #pour chaque hyperarete
        c = Node(h.getName()) #l'hyperarete devient un noeud
        incidenceG.appendNode(c) #qu'on ajoute au graphe d'incidence
        for n in h.getNodes(): #et auquel chaque noeud de l'hyperarete est reliée
            incidenceG.makePointNode(c, n)
    return incidenceG

def primalGraph(graph):
    """
    Retourne le graphe primal de l'hypergraphe passé en paramètre, c'est à dire le graphe où les sommets appartenants à la même hyper-arête
    sont reliés entre eux
    """
    primal = Graph()
    for node in graph.nodes:    #pour chaque noeud de l'hypergraphe
        primal.appendNode(node) #on ajoute le noeud au graphe primal
        for hyperArete in node.getHyperAretes(): #pour chaque hyperarete dans les hyperaretes de ce noeud
            for otherNode in hyperArete.getNodes(): # pour chaque noeud de cette hyperarete
                primal.makePointNode(node, otherNode) #on l'ajoute au graphe primal
    return primal

def dualGraph(graph):
    """
    Retourne l'hypergraphe dual de l'hypergraphe passé en parametre, c'est-à-dire où ses noeuds et ses aretes on été permutés
    """
    dual = HyperGraph(graph.getName()+"*", [], [])
    for node in graph.getNodes():
        newNodes = [] #on crée les nouveaux noeuds, anciennes aretes
        for h in node.getHyperAretes():
            c = HyperNode(h.getName())
            newNodes.append(c)
            dual.addNode(c)
        dual.addHyperArete(HyperArete(str(node.getValue()), newNodes)) #On ajoute la nouvelle arete au graphe dual
    return dual

def isCordal(graph):
    """
    Renvoie True si le graphe est cordal (ie. si tous ses cycles de 4 noeuds ou plus sont cordaux), False sinon
    """
    pass

def isAlphaAcyclic(graph):
    """
    Renvoie True si le graphe est aplha-acyclique (ie. si son graphe primal est cordal, et que toute clique maximale de taille 2 ou plus
    est une hyper-arête dans l'hypergraphe), False sinon
    """

def test():
    H = initG()
    print("Test des fonctions du fichier Functions.py", sep="", end="\n______________________________________\n")
    print("Graphe\n", H, end="\n______________________________________\n")
    print("Graphe d'incidence\n",incidenceGraph(H), sep="", end="\n______________________________________\n")
    print("Graphe primal\n", primalGraph(H), sep="", end="\n______________________________________\n")
    print("Graphe dual\n", dualGraph(H), sep="", end="\n______________________________________\n")
if __name__=="__main__":
    test()
