Steps towards analysing stop words(similar for both Hindi and Bahasa):

1. Extract data from the wiki dumps in json format. 

2. Run script_x.py to create a nice structured list of folders with names new_final_x.py with all docs separated and given a document ID.

3. Finally, run stopwordextractor.py and redirect the output to new_x_words.

x=hindi, bahasa depending on which you want to use.

APPROACH:

Stop words are those words which occur a lot of times, in a document and also across all documents.

I tried to combine term frequency of a word with that of its document-frequency, multiplying the values to form a hashmap of tf-df values.
Ranking the top 25 words then gives us the stopwords.
