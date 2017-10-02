class Node:
	def __init__(self):
		self.child=[None].36
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = Node()

	def index(self,ch):
		if ord(ch)>=97 and ord(ch)<=122:
			return ord(ch)-ord('a')
		else:
			return 25+ord(ch)-ord('0')

	def insert(self,ele):
		l = len(ele)
		curr = self.root
		for i in range(l):
			idx = self.index(ele[i])
			if curr.child[idx]!=None:
				curr.child[idx]=Node()

			curr = curr.child[idx]

		curr.isEnd = True

	def search(self,key):
		curr = self.root
		l = len(key)
		for i in range(l):
			idx = self.index(key[i])
			if curr.child[idx]==None:
				return False
			curr = curr.child[idx]

		return curr.isEnd and curr!=None

if __name__=='__main__':
	trie=[]
	for k in range(0,36):
		t = Trie()
		keys.append(t)
	keys=[]
	for term in keys:
		if ord(term[0])>=97 and ord(term[0])<=122:
			idx = ord(term[0])-ord('a')
			trie[idx].insert(term)
		else:
			idx=25+ord(term[0])-ord(0)
			trie[idx].insert(term)	