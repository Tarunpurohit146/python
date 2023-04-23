import os
ex={'docx':'DOCfile','txt':'Text','pdf':'PDF_file'} #Add more extension based on your choice
d=os.listdir()
for i in d:
   if i.split('.')[-1] in ex:
   	if not os.path.isdir(ex[i.split('.')[-1]]):
   		os.mkdir(ex[i.split('.')[-1]])
   	os.system(f'mv {i} {ex[i.split(".")[-1]]}')