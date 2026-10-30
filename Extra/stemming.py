import nlkt 
from nltk.stem import PorterStemmer

ws = PorterStemmer()

print(ws.stem('eating'))
print(ws.stem('running'))
print(ws.stem('agreed'))
print(ws.stem('agreeing'))
print(ws.stem('agreeable'))
