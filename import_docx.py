from docx import Document
import re
import string

# import numpy
import numpy as np

# import word_tokenize & FreqDist from NLTK
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist

dokumen = Document('CV.docx')

par_array = []

par = dokumen.paragraphs

for para in par:
    text=str(para.text.lower())
    remove_angka = re.sub(r"\d+", "", text)
    remove_punctuation = remove_angka.translate(str.maketrans("","",string.punctuation))
    par_array.append(remove_punctuation.split())

print(par_array)

# tokenize = []
# for i in par_array:
#     if len(i) > 0:
#         tokenize.append(i)

# list_par = []
# for i in range(len(tokenize)):
#     for a in range(len(tokenize[i])):
#         list_par.append(tokenize[i][a])

# print(list_par)





