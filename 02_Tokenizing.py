import string
import re
from nltk.tokenize import word_tokenize


sentence = """Obat berbentuk pil buatan Pfizer Inc. bernama Paclovid. Saat ini, 
pihak Pfizer berencana untuk menyerahkan data sesegera mungkin kepada Food and Drug Administration (FDA) 
untuk meminta otorisasi agar obat tersebut digunakan di Amerika Serikat. Pil Pfizer telah diuji pada pasien berisiko 
tinggi, berisiko rendah, dan orang-orang yang tinggal serumah dengan pasien terkonfirmasi positif COVID-19."""

# Case Folding
lower_sentence = sentence.lower()


# Tokenizing
tokenize_sentence = re.sub(r"\+d", "", lower_sentence)


print(tokenize_sentence)
