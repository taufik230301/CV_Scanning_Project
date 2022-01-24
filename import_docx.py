from docx import Document
import re
import string
dokumen = Document('CV.docx')

par_array = []
par = dokumen.paragraphs

for para in par:
    text=str(para.text.lower())
    remove_angka = re.sub(r"\d+", "", text)
    remove_punctuation = remove_angka.translate(str.maketrans("","",string.punctuation))
    par_array.append(remove_punctuation.split())

for i in par_array:
    if len(i) > 0:
        print(i)

