from query_processing import query_reduction as qr
from document_processing import document_reduction as dr

runQuery = qr()
filter_query = runQuery.reducedQuery_stopwords()
print(filter_query)
print(runQuery.reducedQuery_stemming(filter_query))

runDoc = dr()
path = '/home/tex/Downloads/wikiextractor/Output1'
runDoc.decReduction(path)


