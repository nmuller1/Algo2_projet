#Partie 2

class Node:
	def __init__(self, v, h=[]):
		self.value = v
		self.hyperAretes = h
	def __str__(self):
		return str(self.value)
	def getValue(self):
		return self.value
	def setValue(self, v):
		self.value = v
	def appendHyperArete(self, h):
		self.hyperAretes.append(h)	
	
class HyperArete:
	def __init__(self, *nodes):
		self.nodes = nodes
		for i in self.nodes:
			i.appendHyperArete(self)
	def __str__(self):
		res = "Cette hyper-arête contient les noeuds suivants: \n"
		for i in self.nodes:
			res+=". "+str(i)+"\n"
		return res
	

if __name__ == "__main__":
	a, b, c, d = Node(1), Node(2), Node(3), Node(4)
	k = HyperArete(a, b, c)
	l = HyperArete(b, c, d)
	print(k)
	print(l)