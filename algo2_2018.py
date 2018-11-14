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

from random import randint

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
	
def test_enonce():
	arbre = tree(2)
	a = tree(-5)
	b = tree(-1)
	c = tree(4)
	d = tree(-1)
	e = tree(-1)
	f = tree(-1)
	g = tree(-1)
	h = tree(2)
	i = tree(4)
	j = tree(-5)
	k = tree(1)
	l = tree(-1)
	m = tree(3)
	n = tree(-1)
	arbre.add(a)
	arbre.add(b)
	d.add(i)
	d.add(j)
	g.add(k)
	j.add(l)
	m.add(n)
	j.add(m)
	a.add(c)
	a.add(d)
	a.add(e)
	b.add(f)
	b.add(g)
	b.add(h)
	print(arbre)
	print(max_subtree(arbre))
	
def test_negatif():
	arbre = tree(-2)
	b = tree(-4)
	c = tree(-1)
	d = tree(0)
	e = tree(-5)
	arbre.add(b)
	arbre.add(c)
	b.add(d)
	b.add(e)
	print(arbre)
	print(max_subtree(arbre))

def generateRandomTree():
    """
    Génere aléatoirement un arbre, d'une hauteur et d'un nombre de noeuds aléatoire
    """
    arbre = tree(randint(-20,20))
    numberOfChilds = randint(0,3)
    for i in range(numberOfChilds) :
    	arbre.childs.append(generateRandomTree())
    return arbre

if __name__ == "__main__":
	arbre = generateRandomTree()
	print(arbre)
	max_subtree(arbre)