class Node:
	def __init__(self):
		self.child=[None].38
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = Node()

	def index(self,ch):
		if (hex(ch)-hex('ا'))>=0 and (hex(ch)-hex('ا'))<=28:
			return (hex(ch)-hex('ا'))
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
	for k in range(0,38):
		t = Trie()
		keys.append(t)

	# fetch the terms from the docs
	keys=[]
	for term in keys:
		if (hex(ch)-hex('ا'))>=0 and (hex(ch)-hex('ا'))<=28:
			idx = (hex(ch)-hex('ا'))
			trie[idx].insert(term)
		else:
			idx=27+(hex(ch)-hex('ا'))
			trie[idx].insert(term)