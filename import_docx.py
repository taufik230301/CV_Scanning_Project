from docx import Document
import re
import string
import nltk

# import numpy
import numpy as np

# import word_tokenize & FreqDist from NLTK
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist

dokumen = Document('CV.docx')

array_keyword = ["html", "postgresql", "design", "indonesia", "javascript"]

par_array = []

par = dokumen.paragraphs

tokenize = []

key_word = []
for x in range(len(array_keyword)):
    text = str(array_keyword[x].lower())
    remove_angka = re.sub(r"\d+", "", text)
    remove_punctuation = remove_angka.translate(str.maketrans("","",string.punctuation))
    lowercase_sentence = ''.join(remove_angka.split())
    
    key_word.append(lowercase_sentence)
print(key_word)


for para in par:
    text=str(para.text.lower())
    remove_angka = re.sub(r"\d+", "", text)
    remove_punctuation = remove_angka.translate(str.maketrans("","",string.punctuation))
    lowercase_sentence = remove_punctuation.strip()
    lowercase_sentence = re.sub('\s+',' ',lowercase_sentence)
    tokens = nltk.tokenize.word_tokenize(lowercase_sentence)

    if len(tokens) > 0:
        tokenize.append(tokens)
    



list_par = []
for i in range(len(tokenize)):
    for a in range(len(tokenize[i])):
        if tokenize[i][a] not in list_par:
            list_par.append(tokenize[i][a])


count = 0
for x in range(len(key_word)):
    for y in range(len(list_par)):
        if key_word[x] == list_par[y]:
            count += 1


result = count / len(array_keyword) * 100
print("Kencocokan kandidiat dengan key word yang anda cari")
print(str(int(result)) + "%")
print("Data di CV")







