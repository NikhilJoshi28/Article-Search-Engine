import os
import json

class TfIdf:
	def __init__(self, processed_corpus_path):
		self.processed_corpus_path = processed_corpus_path
		self.tf()
	
	def tf(self):
		for folder in os.listdir(self.processed_corpus_path):
			dir_path = os.path.join(os.sep, self.processed_corpus_path, folder)
			for a_file in os.listdir(dir_path):
				file_path = os.path.join(os.sep, dir_path, a_file)
				term_freq={}
				with open (file_path, 'r') as infile:
					words = infile.readlines()
					for word in words:
						term_freq[word[:-1]] = 0
					for word in words:
						term_freq[word[:-1]] += 1
				with open (file_path, 'w', encoding='utf8') as dumpfile:
					json.dump(term_freq, dumpfile, ensure_ascii=False)
			print(folder+" tf'ed")

if __name__=='__main__':
	processed_corpus_path = '/home/dennis/Documents/dev/IR/processdata'
	# processed_corpus_path = '/home/dennis/Documents/dev/IR/WES/arwiki_parser/processed_corpus'
	TfIdf(processed_corpus_path)