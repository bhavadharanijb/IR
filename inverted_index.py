from nltk.corpus import stopwords
import string
# nltk.download("stopwords")
import re
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
# nltk.download('punkt')
# nltk.download("stopwords")
Stopwords = set(stopwords.words('english'))
from nltk.stem import PorterStemmer

inp = {"Doc1":"Dog is a very , 3 faithful animal", "Doc2": "Cat is a. 45 weird animal ", "Doc3": "	I love to eat chicken"}
ps = PorterStemmer()

def preprocessing(sentence):
	text = sentence.lower()
	text = re.sub(r'[^\w\s]', '', text)
	text = re.sub(r'\d+', '', text)
	tokenized_words_with_stopwords = word_tokenize(text)
	tokens = [word for word in tokenized_words_with_stopwords if word not in Stopwords]
	for j in range(len(tokens)):
		tokens[j] = ps.stem(tokens[j])
	return tokens

terms = []
converted = {}
inv_index = {}
for i in inp:
	tokens = preprocessing(inp[i])
	terms = list(set(terms).union(set(tokens)))
	converted[i] = tokens
	for j in tokens:
		if(j not in inv_index):
			inv_index[j] = {i,}
		else:
			inv_index[j] = inv_index[j].union({i,})


def query(sentence):
	tokens = preprocessing(sentence)
	out = set()
	for i in tokens:
		if(i in inv_index):
			out = out.union(inv_index[i])
	print(out)



print(inv_index)
query("dog is animal")







