from docxlatex import Document

doc = Document("anatomy-and-physiology-2e/00-preface.docx")
text = doc.get_text()
print(text)