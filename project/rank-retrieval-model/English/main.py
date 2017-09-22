from query_processing import query_reduction as qr
from document_processing import document_reduction as dr
from indexing import indexing as indx


runQuery = qr()
filter_query = runQuery.reducedQuery_stopwords()
#print(filter_query)
#print(runQuery.reducedQuery_stemming(filter_query))

"""
#this line is used for document processing which includes stemming, removal of stop words, case folding and removal of punctuation
runDoc = dr()
path = '/home/tex/Downloads/wikiextractor/Output1'
runDoc.decReduction(path)

"""
runIndexing = indx()
runIndexing.file_indexing()
