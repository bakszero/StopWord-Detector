from pathlib import Path 
import json
import os
        



table = []
num = 0
file_list=['./out.txt']
for f in file_list:
    with open(f, encoding='utf-8') as data_file:
        for line in data_file:
            table.append(json.loads(line))

    for row in table:
        new_file = open('./new_final_bahasa_extracted/'+str(num), 'w+')
        new_file.write(row['desc'])
        new_file.close()

        num+=1
    table =[]
