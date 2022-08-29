# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:12:44 2022

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

path = r"C:\Users\bhava\OneDrive\Desktop\sem-9\Lab\IR\WS-1\dataset"
os.chdir(path)


key_words = ['AND', 'OR', 'NOT']

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
                temp.append(j.lower())
        temp=set(temp)
        temp=list(temp)
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
            temp.append(j)
    data_without_stopwords.append(temp)
        
data_stemming = []

for i in data_without_stopwords:
    temp = []
    for j in i:
        word = ps.stem(j)
        temp.append(word)
    data_stemming.append(temp)
    
inverted_index = defaultdict(list)

cnt = 0

for i in data_stemming:
    cnt += 1
    for j in i:
        if j not in inverted_index:
            inverted_index[j] = [cnt]
        else:
            inverted_index[j].append(cnt)
    
print(inverted_index)
    
q=list(input("Enter the query: ").split(" "))

print(q)

print("The Available Boolean Operations: ")
print("1. And ")
print("2. OR ")
print("3. NOT ")

print("Enter your choice: ")
n=int(input())

if(n==1):

#boolean Query
    boolean_query=[]
    return_Doc=set(inverted_index[q[0]])
    ans=set()
    for i in q:
        boolean_query.append(inverted_index[i])
        ans=return_Doc & set(inverted_index[i])
        return_Doc=ans
        
    print(boolean_query)
    print("Selected docs: ", return_Doc)

elif(n==2):
    boolean_query=[]
    return_Doc=set(inverted_index[q[0]])
    ans=set()
    for i in q:
        boolean_query.append(inverted_index[i])
        ans=return_Doc | set(inverted_index[i])
        return_Doc=ans
        
    print(boolean_query)
    print("Selected docs: ", return_Doc)
#return the document

elif(n==3):
    boolean_query=[]
    return_Doc=set(inverted_index[q[0]])
    ans=set()
    for i in q:
        boolean_query.append(inverted_index[i])
        ans=return_Doc & set(inverted_index[i])
        return_Doc=ans
    final=set(inverted_index[q[0]])-return_Doc   
    print(boolean_query)
    print("Selected docs: ", final)

else:
    print("Invalid Option")
