import pickle

str = raw_input()

class autocomplete:
	def __init__(self,str):
		self.filename='/home/nikhil/wikipediasearch/'+str[0]+'.pkl'

