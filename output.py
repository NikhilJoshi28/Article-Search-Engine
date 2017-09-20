import os 

path="/home/tex/Downloads/wikiextractor/Output"

folder_list = [x[0] for x in os.walk(path)]

for each_dir in folder_list[1:][:1]:
	each_file = os.listdir(each_dir)
	#print(len(each_file))
	if len(each_file) > 0:
		for file in each_file[:1]:
			file_path = each_dir+'/'+file
			print(file_path)
			source = open(file_path,'w').read()
			try:
				value = source.split('<doc')[1].split('</doc>')[0]
				print(value)
			except Exception as e:
				print(e)