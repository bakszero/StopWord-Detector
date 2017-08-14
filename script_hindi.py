from pathlib import Path 
import json
import os
rootdir = './hindi_data'

file_list=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_list.append((os.path.join(subdir,file)))
        


print (file_list)
table = []
num = 0

for f in file_list:
    with open(f, encoding='utf-8') as data_file:
        for line in data_file:
            table.append(json.loads(line))

    for row in table:
        new_file = open('./new_final_hindi_extracted/'+str(num), 'w+')
        new_file.write(row['text'])
        new_file.close()

        num+=1
    table =[]
