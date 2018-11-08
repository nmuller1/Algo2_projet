from partie2 import *

#Fichier qui gère les fonctions, on liera tout plus tard mais comme ça c'est plus clair.


def incidenceGraph(graph):
    """
    Cette fonction renvoie le graphe d'incidence
    """
    incidenceG = Graph()
    for n in graph.getNodes(): #pour chaque Noeud #l'hyperarete devient un noeud
        incidenceG.appendNode(n) #qu'on ajoute au graphe d'incidence
        for h in n.getHyperAretes(): #et auquel chaque hyperArete du noeud est reliée
            c = HyperNode(h.getName())
            incidenceG.makePointNode(n, c)
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
            for otherNode in hyperArete.getNodes():# pour chaque noeud de cette hyperarete
                if otherNode is not node:
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
        dual.addHyperArete(HyperArete("E"+str(node.getValue()), newNodes)) #On ajoute la nouvelle arete au graphe dual
    return dual

def isCordal(graph):
    """
    Renvoie True si le graphe est cordal (ie. si tous ses cycles de 4 noeuds ou plus sont cordaux), False sinon
    --> Fulkerson et Gross
    """
    pass

def getMaximalClique(graph):
    """
    Renvoie une liste contenant les cliques maximales de taille 2 ou plus de l'hypergraphe passé en parametre, une liste vide si il
    n'en existe pas
    --> Bron-Kerbosch
    """
    pass

def getCycles(graph):
    """
    Renvoie les cycles de 4 noeuds ou plus
    """
    pass

def isAlphaAcyclic(graph):
    """
    Renvoie True si le graphe est aplha-acyclique (ie. si son graphe primal est cordal, et que toute clique maximale de taille 2 ou plus
    est une hyper-arête dans l'hypergraphe), False sinon
    """
    pass

def test():
    H = initG()
    print("Test des fonctions du fichier Functions.py", sep="", end="\n______________________________________\n")
    print("Graphe\n", H, sep="", end="\n______________________________________\n")
    print("Graphe d'incidence\n",incidenceGraph(H), sep="", end="\n______________________________________\n")
    print("Graphe primal\n", primalGraph(H), sep="", end="\n______________________________________\n")
    print("Graphe dual\n", dualGraph(H), sep="", end="\n______________________________________\n")
if __name__=="__main__":
    test()
