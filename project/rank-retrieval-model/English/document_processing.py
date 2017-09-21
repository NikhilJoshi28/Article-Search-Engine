from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os

class document_reduction:
    def decReduction(self,path):
        dir_list = [x[0] for x in os.walk(path)]
        #print(dir_list)
        file_list = os.listdir(dir_list[0])
        #print(len(file_list))
        for file in file_list[:1]:
            file_path = path+'/'+file
            print(file_path)
            try:
                file_source = open(file_path,'r').read()
                #print(file_source)
                filtered_doc = self.remove_stopwords(file_source)
                print(len(filtered_doc))
            except Exception as e:
                print(file_source+" Not Opening")

            #print(file)

    def remove_stopwords(self,doc):

        t_words = word_tokenize(doc)
        punctuations =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',"''",'``', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@','[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        words = []
        #removing punctuations
        for w in t_words:
            if w not in punctuations:
                words.append(w)

        stop_words = set(stopwords.words("english"))
        filtered_doc = []

        """
        #removing all stop words insted of retaining three adjecent stop words
        for w in words:
            if w not in stop_words:
                filtered_doc.append(w)

        """
        for w in range(len(words)):
            if words[w] not in stop_words:
                filtered_doc.append(words[w])
            elif w<len(words)-2 and words[w] in stop_words and words[w+1] in stop_words and words[w+2] in stop_words:
                filtered_doc.append(words[w])
            elif w>0 and w<len(words)-1 and words[w] in stop_words and words[w+1] in stop_words and words[w-1] in stop_words:
                filtered_doc.append(words[w])
            elif w>1 and words[w] in stop_words and words[w-1] in stop_words and words[w-2] in stop_words:
                filtered_doc.append(words[w])

        return filtered_doc

    def porter_stemmer(self,doc_list):
        ps = PorterStemmer()
        Stemmed_doc = []
        for w in doc_list:
            Stemmed_doc.append(ps.stem(w))

        return Stemmed_doc