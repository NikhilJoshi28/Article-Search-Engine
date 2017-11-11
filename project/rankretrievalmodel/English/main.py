#from query_processing import query_reduction as qr
#from document_processing import document_reduction as dr
#from indexing import indexing as indx

import json
import math

runQuery = qr()
filter_query = runQuery.reducedQuery_stopwords()
#print(filter_query)
#print(runQuery.reducedQuery_stemming(filter_query))


#this line is used for document processing which includes stemming, removal of stop words, case folding and removal of punctuation
runDoc = dr()
path = '/home/tex/Downloads/wikiextractor/Output1'
runDoc.decReduction(path)



runIndexing = indx()
runIndexing.file_indexing()


class QueryProcessor:

	# load the inverted index and inverse document frequency file
	def __init__(self,addr_invert_idx,addr_idf):
		self.scores = {}
		self.q_score = {}
		with open(addr_invert_idx) as json_data:
			self.inver_idx = json.load(json_data)
			json_data.close()

		with open(addr_idf) as json_data:
			self.idf = json.load(json_data)
			json_data.close()

	# generate the vector in the vector space model corresponding to query
	def score_query(self,input_query):
		self.query = input_query.split(' ')
		self.mod = 0
		for i in range(0,len(self.query)):
			if self.query[i] in self.q_score.keys():
				continue
			else:
				ct = 0
				for j in range(i,len(self.query)):
					if(self.query[j]==self.query[i]):
						ct=ct+1
				self.q_score[query[i]] = ct
				self.mod = self.mod + ct*ct

		for term in self.q_score:
			self.q_score[term] = (self.q_score)/math.sqrt(self.mod)

	"""folder_addr containing the tf of individual docs. Generate the dict containing the doc-Id of all the docs containing any of the terms in the query.
	Using the vector representing the query and tf-idf value of the docs determine the proximity between the vector representing the query and vector representing
	the docs(cosine similarity)"""
	def score_docs(self,folder_addr):
		for term in self.q_score.keys():
			for j in range(0,len(self.inver_idx[term])):
				if self.inver_idx[term][j] in self.scores.keys():
					continue
				else:
					self.scores[self.inver_idx[term][j]] = 0

		for doc in self.scores.keys():
			for term in self.query:
				with open(folder_addr+'/'+doc) as json_data:
					self.doc_indx = json.load(json_data)
					json_data.close()
				self.score[doc] = self.score[doc] + self.q_score[term]*(math.log(1+self.doc_indx[term])*self.idf[term])

	"""returns the dictionary containing all the docs containing any of the terms sorted in increasing order of closeness to the query"""
	def return_docs(self):
		sorted(self.score.values())
		return self.score

if __name__=='__main__':
	input_query = raw_input()
	query = input_query.split()
	with open('/home/tex/Documents/IR/Inverted_Index/inverted_indx.txt') as json_data:
		inverted_index = json.load(json_data)
		json_data.close()

	docs = []
	siz = len(query)

	idx = 0

	for i in range(1,siz):
		if len(inverted_index[query[i]])<len(inverted_index[query[idx]]):
			idx = i

	for i in range(0,len(inverted_index[query[idx]])):
		docs.append(inverted_index[query[idx]][i])

	# returns the list of docs corresponding to give query assuming there is no need for any spell correction	
	# docs is the required list of documents
	for i in range(0,siz):
		if i!=idx:
			ans = []
			for j in range(0,len(docs)):
				for k in range(0,len(inverted_index[query[i]])):
					if docs[j]==inverted_index[query[i]][k]:
						ans.append(docs[j])

			docs[:] = []
					
			for j in range(0,len(ans)):
				docs.append(ans[j])
				
	print(docs)

	process = QueryProcessor()
	process.score_query(input_query)
	process.score_docs()
	docs = process.return_docs()