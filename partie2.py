#Partie 2

class Node:
	def __init__(self, value, hyperAretes=[]):
		"""
		Value : valeur du noeud
		hyperAretes : hyper-arêtes qui contiennent le noeud
		"""
		self.value = value
		self.hyperAretes = hyperAretes
		
	def __str__(self):
		return str(self.value)
		
	def getValue(self):
		return self.value
		
	def setValue(self, v):
		self.value = v
		
	def appendHyperArete(self, h):
		"""
		Permet d'annoncer que le noeud appartient à l'hyper-arête h
		"""
		self.hyperAretes.append(h)	
	
class HyperArete:
	def __init__(self, *nodes):
		"""
		nodes : les noeuds qui sont contenus dans l'hyper-arête
		Ceux-ci sont modifiés pour indiquer qu'ils sot-nt contenus dans l'hyper-arête
		"""
		self.nodes = nodes
		for i in self.nodes:
			i.appendHyperArete(self)
	def __str__(self):
		res = "Cette hyper-arête contient les noeuds suivants: \n"
		for i in self.nodes:
			res+=". "+str(i)+"\n"
		return res

class HyperGraph:
	def __init__(self, *nodes, *hyperAretes):
		self.nodes = nodes
		self.hyperAretes = hyperAretes
	

if __name__ == "__main__":
	a, b, c, d = Node(1), Node(2), Node(3), Node(4)
	k = HyperArete(a, b, c)
	l = HyperArete(b, c, d)
	print(k)
	print(l)