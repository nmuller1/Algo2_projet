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

def isConnexe(graph, n1, n2):
    """
    Retourne True si n1 et n2 sont connexes, False sinon (dans un graphe normal)
    """
    res = False
    for hyperArete in n1.getHyperAretes():
        res = res or (n2 in hyperArete.getNodes())
    return res

def isComplet(graph):
    """
    Renvoie True si le graphe est complet, False sinon
    """
    res = True
    for n in graph.getNodes():
        for m in graph.getNodes():
            res = res and isConnexe(graph, n, m)
    return res

def isCordal(graph):
    """
    Renvoie True si le graphe est cordal (ie. si tous ses cycles de 4 noeuds ou plus sont cordaux), False sinon
    --> Fulkerson et Gross
    """
    pass

def getMaximalCliqueFromNode(n, graph):
    """
    Renvoie une liste contenant la clique maximale de taille 2 ou plus du graphe passé en parametre, partant du noeud n, une liste vide si il
    n'en existe pas
    """
    res = Graph()
    res.appendNode(n, graph.getVoisins(n))
    for noeud in (graph.getNodes().keys()):
        res.appendNode(noeud, graph.getVoisins(noeud))
        if not isComplet(res):
            res.delNode(noeud)
    return res
    
def getMaximalCliques(graph):
    p = []
    maxi = 2
    for noeud in graph.getNodes():
        maxClique = getMaximalCliqueFromNode(noeud, graph)
        if maxClique.size()==maxi and maxClique not in p:
            p.append(maxClique)
        elif maxClique.size()>maxi:
            p = [maxClique]
            maxi = maxClique.size()
    return p

def isCliqueHyperArete(clique, hyperGraph):
    res = False
    for hyperArete in hyperGraph.hyperAretes:
        temp = True
        for p in list(clique.nodes):
            temp = temp and p in hyperArete.nodes
        for q in hyperArete.nodes:
            temp = temp and p in list(clique.nodes)
        res = res or temp
        if res:
            break
    return res

def areCliquesHyperAretes(cliques, hyperGraph):
    res = True
    for clique in cliques:
        res = res and isCliqueHyperArete(clique, hyperGraph)
    return res

def isInSubset(liste, el):
    p=-1
    for i in range(len(liste)):
        if el in liste[i]:
            p = i
    return p

def LexOrder(graph):
    """
    Réalise un Lexicographic breadth-first search sur le graphe passé en paramètre
    """
    E = [list(graph.getNodes())]
    output = []
    while len(E)>0:
        v = E[0].pop() # Le dernier élément de la premiere liste de E
        if len(E[0])==0:
            del E[0]
        output.append(v)
        replaced = [False for i in E]
        for voisin in graph.getVoisins(v):
            subSet = isInSubset(E, voisin) #subSet contient l'indice où se trouve le voisin
            if subSet !=-1:
                if replaced[subSet]==False: #Si on a pas encore crée de T pour ce subset
                    T = []
                    replaced[subSet] = T
                    E.insert(subSet, T) #on insere T juste avant S
                    replaced.insert(subSet, False) #on met dans replaced (au correspondant de T), False (il n'a pas encore changé, lui)
                    subSet += 1
                else:
                    T = replaced.index(replaced[subSet]) #dans replaced, la case correspondant a S contient T
                    replaced.insert(subSet, replaced[T])
                    E.insert(subSet, E[T])
                    del replaced[T]
                    del E[T]
                w = E[subSet].pop(E[subSet].index(voisin))
                if len(E[subSet])==0:
                    del E[subSet]
                E[subSet-1].append(w)
    return output

def findClosestVoisin(graph, v, ordered):
    """
    Renvoie la distance entre l'indice du voisin le plus proche de v et v dans ordered
    """
    distance = -1
    for p in graph.getVoisins(ordered[v]):
        if p in ordered[:v]:
            dist = v-ordered.index(p)
            if dist<distance or distance==-1:
                distance = dist
    return distance

def getSubSetVoisinsPrevious(graph, v, ordered, excl = None):
    """
    Renvoie le sous-ensemble des voisins de v précédants v dans ordered
    """
    res = []
    for i in graph.getVoisins(ordered[v]):
        if i in ordered[:v] and i!=excl:
            res.append(i)
    return res

def isSubSet(x, y):
    """
    Renvoie True si x est sous-ensemble de y, False sinon
    """
    res = True
    for i in x:
        res = res and i in y
    return res

def isChordal(graph):
    ordered = LexOrder(graph)
    chordal = True
    for v in range(len(ordered)):
        w = findClosestVoisin(graph, v, ordered)
        if w != -1:
            w = v-w
            subv = getSubSetVoisinsPrevious(graph, v, ordered, excl=ordered[w])
            subw = getSubSetVoisinsPrevious(graph, w, ordered)
            chordal = chordal and isSubSet(subv, subw)
    return chordal

def isAlphaAcyclic(graph):
    """
    Renvoie True si le graphe est aplha-acyclique (ie. si son graphe primal est cordal, et que toute clique maximale de taille 2 ou plus
    est une hyper-arête dans l'hypergraphe), False sinon
    """
    p = primalGraph(graph)
    return isChordal(p) and areCliquesHyperAretes(getMaximalCliques(p), graph)

def isHyperTree(graph):
    return isAlphaAcyclic(dualGraph(graph))

def test():
    H = initH()
    print("Test des fonctions du fichier Functions.py", sep="", end="\n______________________________________\n")
    print("Graphe\n", H, sep="", end="\n______________________________________\n")
    print("Graphe d'incidence\n",incidenceGraph(H), sep="", end="\n______________________________________\n")
    p = primalGraph(H)
    print("Graphe primal\n", p, "\n", sep="", end="\n______________________________________\n")
    print("Graphe dual\n", dualGraph(H), sep="", end="\n______________________________________\n")
    print("Teste si les noeuds v2 et v5 sont connexes: ", isConnexe(H, H.getNodes()[1], H.getNodes()[4]), sep="", end="\n______________________________________\n")
    print("Teste si les noeuds v1 et v4 sont connexes: ", isConnexe(H, H.getNodes()[0], H.getNodes()[3]), sep="", end="\n______________________________________\n")
    print("isAlphaAcyclic:", isAlphaAcyclic(H), end="\n______________________\n")
    print("isHyperTree: ", isHyperTree(H), end="\n______________________\n")
if __name__=="__main__":
    test()
