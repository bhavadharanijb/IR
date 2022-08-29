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

inp = {1:"Dog is a very , 3 faithful animal", 2: "Cat is a. 45 weird animal ", 3: "	I love to eat chicken"}
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
boolean = {}
for i in inp:
	tokens = preprocessing(inp[i])
	print(tokens)
	for j in tokens:
		if (j not in boolean):
			arr = ["0" for j in range(len(inp))]
			arr[i-1] = "1"
			boolean[j] = arr
		else:
			arr = boolean[j]
			arr[i-1] = "1"
			boolean[j] = arr


def query(sentence):
	tokens = preprocessing(sentence)
	out = int("1"*len(inp),2)
	for i in tokens:
		if(i in boolean):
			print(int("".join(boolean[i]), 2))
			out = out & int("".join(boolean[i]), 2)

	print(str(out))



print(boolean)
query("dog is animal")

