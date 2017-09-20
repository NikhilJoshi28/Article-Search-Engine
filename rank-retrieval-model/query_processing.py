import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class query_reduction:
    def reducedQuery(self):
        query = "and and and rank of retrieval and model in in in information retrieval for searching of of "
        words = word_tokenize(query)
        stop_words = set(stopwords.words("english"))
        filtered_query = []
        for w in range(len(words)):
            if words[w] not in stop_words:
                filtered_query.append(words[w])
            elif w==len(words)-1 and words[w-1]==words[w]:
                filtered_query.append(words[w])
            elif words[w] in stop_words and (words[w+1] in stop_words or words[w-1] in stop_words) :
                filtered_query.append(words[w])

        return filtered_query
