#from query_processing import query_reduction as qr
#from document_processing import document_reduction as dr
#from indexing import indexing as indx

import json

"""
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
"""

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

