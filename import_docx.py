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

par_array = []

par = dokumen.paragraphs

tokenize = []

for para in par:
    text=str(para.text.lower())
    remove_angka = re.sub(r"\d+", "", text)
    remove_punctuation = remove_angka.translate(str.maketrans("","",string.punctuation))
    tokens = nltk.tokenize.word_tokenize(remove_punctuation)
    freq_tokens = nltk.FreqDist(tokens)
    if len(tokens) > 0:
        tokenize.append(freq_tokens.most_common())
    
print(tokenize)


# tokenize = []
# for i in par_array:
#     if len(i) > 0:
#         tokenize.append(i)

# list_par = []
# for i in range(len(tokenize)):
#     for a in range(len(tokenize[i])):
#         list_par.append(tokenize[i][a])

# print(list_par)





