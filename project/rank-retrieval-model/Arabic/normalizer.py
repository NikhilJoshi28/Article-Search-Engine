import os
import pickle

class Normalizer:
	def __init__(self, corpus_path):
		# initializing stop words and punctuations
		self.ar_stop_words=[]
		with open ("stop_words", 'r') as f:
			sw=[]
			sw = f.readlines();
			f.close()
			for word in sw:
				self.ar_stop_words.append(word[:-1])
				# -1 to remove the '\n' from end of word
		self.ar_stop_words.sort()
		
		self.path = corpus_path
		self.preprocess()

	def preprocess(self):
		"""
		Removes characters of languages other than
		Arabic which got in files during scraping
		"""
		for folder in os.listdir(self.path):
			dir_path = os.path.join(os.sep, self.path, folder)
			for a_file in os.listdir(dir_path):
				file_path = os.path.join(os.sep, dir_path, a_file)
				string=""
				with open (file_path, 'r') as infile:
					lines = infile.readlines()
					for line in lines:
						for char in line:
							asci = ord(char)
							if ((asci <= 1791 and asci >= 1536) or #retain arabic
								 (asci == 32 or asci == 10) or 	   #retain space and \n
								 (asci >= 48 and asci <= 57)):	   #retain numbers
								string+=char
					infile.close()
				with open (file_path, 'w') as outfile:
					outfile.write(string)
					outfile.close()
			print(folder+" processed")

if __name__=='__main__':
	# path = '/home/dennis/Documents/dev/IR/testdata'
	path = '/home/dennis/Documents/dev/IR/WES/arwiki_parser/arabic_corpus'
	Normalizer(path)