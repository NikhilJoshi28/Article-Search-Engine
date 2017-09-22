import os, sys
import json
from collections import defaultdict, OrderedDict

class TfIdf:
	def __init__(self, processed_corpus_path, inverted_index_path, key_ordering):
		self.processed_corpus_path = processed_corpus_path
		self.inverted_index_path = inverted_index_path
		self.key_ordering = key_ordering

	def tf(self):
		"""
		counts and stores the frequency of a term
		in a document and write it to the same
		document in following order:
		{
			termi: n,
			termj: m,
			...
		}
		n, m are frequencies of termi, termj resp.
		in the document currently being processed
		"""
		for folder in os.listdir(self.processed_corpus_path):
			dir_path = os.path.join(os.sep, self.processed_corpus_path, folder)
			for a_file in os.listdir(dir_path):
				file_path = os.path.join(os.sep, dir_path, a_file)
				term_freq={}
				with open (file_path, 'r') as infile:
					words = infile.readlines()
					for word in words:
						term_freq[word[:-1]] = 0 	
						#^ -1 to remove '\n' from the end of the word
					for word in words:
						term_freq[word[:-1]] += 1
				with open (file_path, 'w', encoding='utf8') as dumpfile:
					json.dump(term_freq, dumpfile, ensure_ascii=False)
			print(folder+" tf'ed")

	def inverted_index(self):
		"""
		creates a json file which stores id
		of all documents in which each term
		is present:

		{
			termi:[d1, d2, ...dk],
			termj:[d2, d3, ...dm],
			...
		}
		here terms(termi, termj) and documents
		in their lists both are in increasing 
		order to reduce the search time
		"""
		doc_list = defaultdict(list)
		i=0
		for folder in os.listdir(self.processed_corpus_path):
			dir_path = os.path.join(os.sep, self.processed_corpus_path, folder)
			for a_file in os.listdir(dir_path):
				file_path = os.path.join(os.sep, dir_path, a_file)
				with open (file_path, 'r') as infile:
					freq_dict = json.load(infile)
					for key, value in freq_dict.items():
						doc_list[key].append(a_file)
			i+=1
			print("Size in MB: "+str(sys.getsizeof(doc_list)/(1024*1024))+". "+folder+" "+str(256-i)+" more to go")
		
		words = sorted(doc_list)
		for word in words:
			doc_list[word].sort()

		print("creating inverted index...")
		with open (self.inverted_index_path, 'w') as dumpfile:
			json.dump(doc_list, dumpfile, ensure_ascii=False)
		print("inverted index created!")
		print("creating ordering file...")
		with open (self.key_ordering, 'w') as dumpfile:
			json.dump(words, dumpfile, ensure_ascii=False)
		print("ordering file created!... Done.")
		
		# printing the values after loading on RAM
		# order=[]
		# with open(self.key_ordering, 'r') as infile:
		# 	order = json.load(infile)
		# with open(self.inverted_index_path, 'r') as infile:
		# 	d = json.load(infile)
		# 	for word in order:
		# 		print(word, d[word])

if __name__=='__main__':
	# test
	# processed_corpus_path = '/home/dennis/Documents/dev/IR/processdata'
	# inverted_index_path = '/home/dennis/Documents/dev/IR/inv'
	# sorted_keys = '/home/dennis/Documents/dev/IR/order'
	
	# final
	# processed_corpus_path = '/home/dennis/Documents/dev/IR/WES/arwiki_parser/processed_corpus'
	# inverted_index_path = '/home/dennis/Documents/dev/IR/WES/arwiki_parser/inv'
	# sorted_keys = '/home/dennis/Documents/dev/IR/WES/arwiki_parser/order'
	

	ti = TfIdf(processed_corpus_path, inverted_index_path, sorted_keys)
	# ti.tf()
	# ti.inverted_index()