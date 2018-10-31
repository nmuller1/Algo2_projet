from random import randint

class tree:
	def __init__(self, root):
		self.value = root
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
		check = False
		for i in arbre.childs:
			if not check and arbre.value >= 0:
				check = True
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
if __name__ == "__main__":
	test_enonce()
	print()
	test_negatif()