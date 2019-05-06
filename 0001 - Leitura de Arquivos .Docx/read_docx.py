
# Must have installed docx on yout wheel '-pip install docx'
import docx

import os
import pprint


# Consumes docx file into ::var:doc
doc = docx.Document('document_path/document.docx')
#pprint.pprint(doc.paragraphs)



# Print all text content in doc.paragraphs
for par in doc.paragraphs:
    print(par.text)
