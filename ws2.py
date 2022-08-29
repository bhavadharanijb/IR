# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:58:34 2022

@author: bhava
"""

import nltk
import os
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict
import numpy as np
import math

path = r"C:\Users\bhava\OneDrive\Desktop\sem-9\Lab\IR\WS-2\dataset"
os.chdir(path)

data = []
ps = PorterStemmer()

punc = '''!,=@#$%_()[]{}:;'''

def read_file(file, data):
    with open(file, 'r') as f:
        sentence = f.read().split("\n")
        words = []
        for x in sentence:
            words.append(word_tokenize(x))
        temp = []
        for i in range(len(words)):
            for j in words[i]:
                temp.append(j)
        data.append(temp)
            
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_file(file_path, data)
        

data_without_stopwords = []

for i in data:
    temp = []
    for j in i:
        if j not in stopwords.words() and j != '':
            #w = ''.join(x for x in j if x.isalnum())
            re.sub('[^A-Za-z0-9]+', ' ', j)
            temp.append(j.lower())
    data_without_stopwords.append(temp)
        
data_stemming = []

for i in data_without_stopwords:
    temp = []
    for j in i:
        word = ps.stem(j)
        temp.append(word)
    data_stemming.append(temp)
    
final_unique_words = set()

for i in data_stemming:
    for j in i:
        final_unique_words.add(j)

final_unique_words = list(final_unique_words)
final_unique_words.sort()
doc_cnt = len(data_stemming)
term_cnt = len(final_unique_words)
print(doc_cnt, term_cnt)
#matrix = np.zeros((term_cnt, doc_cnt))
matrix = []

for i in range(doc_cnt):
    dummy = []
    for j in range(term_cnt):
        temp = data_stemming[i].count(final_unique_words[j])
        dummy.append(temp)
    matrix.append(dummy)

print(matrix)

for i in range(doc_cnt):
    row_max = max(matrix[i])
    for j in range(len(matrix[i])):
        matrix[i][j] /= row_max
       
print("\n")
print(matrix)

idf = [0 for i in range(term_cnt)]

for i in range(term_cnt):
    #print(i)
    f_cnt = 0
    for j in range(doc_cnt):
        if matrix[j][i] != 0:
            f_cnt += 1
    if f_cnt == 0:
        idf[i] = 0
    else:
        idf[i] = math.log(doc_cnt / f_cnt)
  
print("\nIDF:")
print(idf)
    
for i in range(term_cnt):
    for j in range(doc_cnt):
        matrix[j][i] *= idf[i]
        
print("\nNew Matrix:")
print(matrix)

#similarity

#q=list(map(int,input("enter the query: ").split(" ")))
q = [1]*term_cnt

n=0
no=1
d1=0
d2=0
d=0
s={}
for k in matrix:
    for i,j in zip(q,k):
        n+=(i*j)
        d1+=i**2
        d2+=j**2
    d1=d1**0.5
    d2=d2**0.5
    d=d1*d2
    s["Doc-"+str(no)]=n/d
    no+=1

s=sorted(s.items(), key=lambda x:x[1],reverse=True)
print("Similarity: ",s)
    