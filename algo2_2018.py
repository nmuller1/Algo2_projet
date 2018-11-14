"""
Projet Algo 2
"""
# *- coding: utf-8 - *-
__author__ = "Noëmie Muller & Pascal Tribel" 
__matricule__ = "000458865 & 000461792"
__date__ = "15/11/2018"
__cours__ = "info"
__asistant__ = "Keno Merckx"

"""
Partie 1 : Sous-arbre de poids Maximum

"""

from random import randint, choice
########################################################################################################################
#Partie 1
class tree:
	def __init__(self, root):
		self.value = root
		self.size = 1
		self.level = 0
		self.parent = None
		self.childs = []

	def __str__(self):
		res = ""
		res += str(self.value)
		if self.childs != []:
			res += "->"
		for i in self.childs:
			res += "[" + str(i) + "]"
		return res

	def add(self, value):
		if value != []:
			sousArbre = value #value doit etre de type tree
			sousArbre.parent = self
			sousArbre.level = self.level + 1
			self.childs.append(sousArbre)

	def get_child(self, number):
		return self.childs[number]
	
	def somme(self):
		res = self.value
		for i in self.childs:
			res += i.somme()
		return res

def max_subtree(arbre):
	"""Retourne le sous-arbre de plus grande valeur de l'arbre passé en paramètre"""
	sous_arbre = []
	if arbre.childs == []: #Si l'arbre est feuille
		sous_arbre = arbre
	else:
		check = False #flag qui indique si la solution a déjà été créée
		for i in arbre.childs:
			if not check and arbre.value >= 0:
				check = True #si le noeud est positif, on le prend toujours
				sous_arbre = tree(arbre.value) 
			k =  max_subtree(i)
			if k!= [] and k.somme() > 0:
				if not check:
					check = True
					sous_arbre = tree(arbre.value)
				sous_arbre.add(k)
	return sous_arbre

def generateRandomTree(level=randint(2, 5)):
    """
    Génere aléatoirement un arbre, d'une hauteur et d'un nombre de noeuds aléatoire
    """
    arbre = tree(randint(-10,10))
    numberOfChilds = randint(1,3)
    for i in range(numberOfChilds) :
        if level>1:
            arbre.childs.append(generateRandomTree(level-1))
    return arbre

def testPartie1():
    print("______Test_de_la_Partie_1______")
    for i in range(5):
        print("Test", i)
        t = generateRandomTree()
        print("L'arbre:", t)
        print("Son sous-arbre maximal:", max_subtree(t))
        print("__________________________________________")
##########################################################################################################################
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
        Value : valeur du noeud
        """
        super().__init__(value) #Pour initialiser la valeur du noeud
        self.hyperAretes = [] #hyper-arêtes qui contiennent le noeud
    
    def appendHyperArete(self, h):
        """
        Indique que le noeud appartient à l'hyper-arête h
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
        Ceux-ci sont modifiés pour indiquer qu'ils sont contenus dans cette nouvelle hyper-arête
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
        for i in self.getNodes():
            if i.getHyperAretes == []:#Pour l'affichage des noeuds qui n'appartiendraient pas à une hyperArete
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

def generateRandomHyperGraph(name):
    """
    Génere aléatoirement un graphe, de taille aléatoire en nombre de noeuds et d'aretes
    """
    numberOfNodes = randint(2, 15)
    nodes = []
    for i in range(numberOfNodes):
        nodes.append(HyperNode(("v"+str(i))))
    numberOfHyperAretes = randint(1, numberOfNodes)
    hyperAretes = []
    for i in range(numberOfHyperAretes):
        nodesChosen = []
        numberOfNodesChosen = randint(1, numberOfNodes)
        while len(nodesChosen)<numberOfNodesChosen:
            c = choice(nodes)
            if c not in nodesChosen:
                nodesChosen.append(c)
        hyperAretes.append(HyperArete("E"+str(i), nodesChosen))
    hyperGraph = HyperGraph(name, nodes, hyperAretes)
    return hyperGraph
                
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
    """
    Renvoie une liste avec les cliques maximales d'un graphe
    """
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
    """
    Renvoie True si la clique passée en paramètre est hyperArete dans l'hyperGraphe, False sinon
    """
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
    """
    Renvoie True si toutes les cliques passées en paramètre sont chacune hyperAretes dans l'hyperGraphe, False sinon
    """
    res = True
    for clique in cliques:
        res = res and isCliqueHyperArete(clique, hyperGraph)
    return res

def isInSubset(liste, el):
    """
    Renvoie l'indice de la sous-liste de liste ou se trouve el, -1 si il n'appartient pas à liste
    """
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
    """
    Renvoie True si le graphe est cordal, False sinon
    """
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
    """
    Renvoie True si l'hyperGraphe est un hyperTree, False sinon
    """
    return isAlphaAcyclic(dualGraph(graph))    

def testPartie2():
    numberOfHyperGraphs=5
    print("______Test_de_la_Partie_2______")
    for i in range(numberOfHyperGraphs):
        H = generateRandomHyperGraph(("My Graph "+str(i)))
        print("L'hyper-graphe:", H, end="\n_____________________\n")
        print("Son hyper-graphe dual:", dualGraph(H), end="\n_____________________\n")
        print("Est-il un hyperTree:", isHyperTree(H), end="\n_____________________\n")

def main():
    testPartie1()
    testPartie2()
if __name__ == "__main__":
    main()
