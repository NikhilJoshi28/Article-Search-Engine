import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class query_reduction:
    def reducedQuery_stopwords(self):
        query = "rank of the retrieval this is and model in information retrieval for searching of and"
        words = word_tokenize(query)
        stop_words = set(stopwords.words("english"))
        filtered_query = []
        for w in range(len(words)):
            if words[w] not in stop_words:
                filtered_query.append(words[w])
            elif w>0 and w<len(words)-1 and words[w] in stop_words and (words[w-1] in stop_words or words[w+1] in stop_words):
                filtered_query.append(words[w])
            elif w==0 and words[w] in stop_words and words[w+1] in stop_words:
                filtered_query.append(words[w])
            elif w==len(words)-1 and words[w] in stop_words and words[w-1] in stop_words:
                filtered_query.append(words[w])
        return filtered_query
