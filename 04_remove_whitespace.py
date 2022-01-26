import string
import re
from nltk.tokenize import word_tokenize
import nltk


sentence = """Obat berbentuk pil buatan Pfizer Inc. bernama Paclovid. Saat ini, 
pihak Pfizer berencana untuk menyerahkan data sesegera mungkin kepada Food and Drug Administration (FDA) 
untuk meminta otorisasi agar obat tersebut digunakan di Amerika Serikat. Pil Pfizer telah diuji pada pasien berisiko 
tinggi, berisiko rendah, dan orang-orang yang tinggal serumah dengan pasien terkonfirmasi positif COVID-19."""

# Case Folding
lower_sentence = sentence.lower()


# Tokenizing
tokenize_sentence = re.sub(r"\+d", "", lower_sentence)

# Remove Punctutation
remove_punctuation_sentence = tokenize_sentence.translate(str.maketrans("","",string.punctuation))


tokens = nltk.tokenize.word_tokenize(remove_punctuation_sentence)

# remove white space
whitespace_remove_sentence = remove_punctuation_sentence.strip()
print("Setelah meremove whitespace")
print(" ")
print(whitespace_remove_sentence)
print("_________")
multiple_whitespace_sentence = re.sub('\s+',' ',whitespace_remove_sentence)
print("Setelah meremove multiple whitespace")
print(" ")
print(multiple_whitespace_sentence)
print("-"*200)
print("Tokenize to Array")
print(" ")
print(tokens)
