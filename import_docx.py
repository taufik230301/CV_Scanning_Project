from docx import Document

dokumen = Document('CV.docx')

par_array = []
par = dokumen.paragraphs

for i in range(len(par)):
    par_array.append(par[i].text)

print(par_array[1])

