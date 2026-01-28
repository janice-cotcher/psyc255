import pypandoc
from pathlib import Path
import os
import aspose.slides as slides
from docxlatex import Document
from pathlib import Path

def createDir(output_dir):
    if not checkDir(output_dir):
            print(f"creating {output_dir}")            
            os.makedirs(output_dir, exist_ok=True)
            print(f"Directory '{output_dir}' ensured to exist.")
    else:
        print(f"{output_dir} already exists")

def slideConvert(input, output):
    # Load the presentation
    presentation = slides.Presentation("input.pptx")
    # Save as PDF
    presentation.save("output.pdf", slides.export.SaveFormat.PDF)


def wordConvert(file, dir):
    doc = Document(file)
    text = doc.get_text()
    output_file = extractName(file, dir, "tex")
    with open(output_file, "w") as output:
        output.write(text)

def checkDir(dir_path):
    directory_path = Path(dir_path)

    if directory_path.is_dir():
        return True
    else:
        return False

def extractName(file, dir, ext):
    file_name_without_ext = Path(file).stem
    new_file = f"{file_name_without_ext}.{ext}"
    full_path = os.path.join(dir, new_file)
    return full_path
