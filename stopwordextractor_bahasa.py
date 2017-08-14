import glob
import math
import codecs
from operator import itemgetter
words = set()

flist = glob.glob('./new_final_bahasa_extracted/*')

for fname in flist[:50000]:
    with codecs.open(fname,encoding='utf-8') as tfile:
        line = tfile.read()
        words=words.union(set(line.split()))
        tfile.close()
#print (words)
words = sorted(words)
#print (words)
term_count = {}
doc_count={}

for doc in flist[:50000]:
    with codecs.open(doc, encoding='utf-8') as docfile:
        #temp_dict = {}
        line = docfile.read()
        docfile.close()

        splitted_line = line.split()
        #splitted_line=line.split('-')

        temp_words = set(splitted_line)
        for word in temp_words:
            temp_count = splitted_line.count(word)
            if word not in term_count:
                term_count[word]=temp_count
            else:
                term_count[word]+=temp_count

            if word in doc_count:
                doc_count[word]+=1
            else:
                doc_count[word]=1

        
'''
doc_count ={}
temp_count =0

temp_doc_count={}
for fdoc in flist[:1000]:
    doc = open(fdoc, "r")
    line = doc.read()
    doc.close()

    line.split()

    count = line.count(str(term))
    doc_count[term]=count
'''

final_words = sorted(doc_count.items(), key=itemgetter(1), reverse=True)
final_term_words = sorted(term_count.items(), key = itemgetter(1), reverse=True)
#print("DOC COUNTS")
for a, b in final_words[:50]:
    pass
    #print ("{0} : {1}".format(a,b))
#print ('\n\n\n\n\n\n\n')
#print ("TERM COUNTS")

for c, d in final_term_words[:50]:
    pass
    #print ("{0} : {1}".format(c,d))


print ('TOP 25 STOPWORDS with score\n\n')

d3={}
def dict_mul(d1, d2):
    
    for k in d1:
        if k in d2:
            d3[k] = d1[k] * d2[k]
    return d3

dict_fin = dict_mul(term_count, doc_count)
sorted_dict_fin = sorted(dict_fin.items(), key = itemgetter(1), reverse=True)

for c, d in sorted_dict_fin[:25]:
    print ("{0} : {1}".format(c,d))
