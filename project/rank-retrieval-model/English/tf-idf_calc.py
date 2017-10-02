import json
import math
import os
import glob

class Tf_Idf:

	def __init__(self,addr_tf,addr_idf):
		"""load the file containing dictionary of term freq and file containing Inverted doc freq"""
		with open(addr_tf) as json_data:
			self.tf = json.load(json_data)
			json_data.close()

		with open(addr_idf) as json_data:
			self.idf = json.load(json_data)
			json_data.close()

	def tf_idf_calc(self):
		"""for each term present in the doc multiply each of the term's freq with inverted doc freq"""
		for term in self.tf:
			try:
				self.tf[term]=math.log(1+self.tf[term],10)*(self.idf[term])
			except Exception as e:
				print(term,e)
				
	def tfidffile(self,new_tf):
		"""store the dictionary of tf-idf values in the form of a json object"""
		try:
			with open(new_tf,'w') as score:
				json.dump(self.tf,score,ensure_ascii=False)
		except Exception as e:
			print (e)


if __name__=='__main__':
	addr = '/home/tex/Documents/IR/Final_Output1000/'
	addr_idf = '/home/tex/Documents/IR/Inverted_Index/idf.txt'
	new_file = '/home/tex/Documents/IR/tf_idf/'
	files = os.listdir('/home/tex/Documents/IR/Final_Output1000/')
	for filename in files:
		print(filename)
		score = Tf_Idf(addr+filename,addr_idf)
		score.tf_idf_calc()
		score.tfidffile(new_file+filename)