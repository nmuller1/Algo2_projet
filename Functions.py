from partie2 import *

#Fichier qui gère les fonctions, on liera tout plus tard mais comme ça c'est plus clair.


def incidenceGraph(graph):
    """
    Cette fonction renvoie un dictionnaire ayant pour clés les hyper-arêtes et pour valeurs la liste des sommets qu'ils contiennent
    """
    incidenceG = {}
    for h in graph.getHyperAretes():
        incidenceG[h] = h.getNodes()
    return incidenceG

def primalGraph(graph):
    """
    Retourne le graphe primal de l'hypergraphe passé en paramètre, c'est à dire le graphe où les sommets appartenants à la même hyper-arête sont reliés entre eux
    """
    primal = Graph()
    for node in graph.nodes:    #pour chaque noeud de l'hypergraphe
        primal.appendNode(node) #on ajoute le noeud au graphe primal
        for hyperArete in node.getHyperAretes(): #pour chaque hyperarete dans les hyperaretes de ce noeud
            for otherNode in hyperArete.getNodes(): # pour chaque noeud de cette hyperarete
                primal.makePointNode(node, otherNode) #on l'ajoute au graphe primal
    return primal

if __name__=="__main__":
    H = initG()
    print(primalGraph(H))
