import json
import math

class Tf-Idf:
	def __init__(self,addr_tf,addr_idf):
		with open(addr_tf) as json_data:
			self.tf = json.load(json_data)
			json_data.close()

		with open(addr_tf) as json_data:
			self.idf = json.load(json_data)
			json_data.close()

	def tf_idf_calc(self):
		for term in self.tf:
			self.tf[term]=math.log(1+self.tf[term],10)*(self.idf[term])

	def tf_idf_file(self,addr_tf):
		with open(addr_tf,'w') as score:
			json.dump(self.tf,score,ensure_ascii=False)


if __name__=='main':

	addr = '/home/nikhil/wikipediasearch/termfrequencydocs'
	files = os.listdir('/home/nikhil/wikipediasearch/termfrequencydocs')
	for filename in files:
		score = Tf-Idf(addr+filename,idf_addr)
		score.tf_idf_calc()
		score.tf_idf_file(addr+filename)
