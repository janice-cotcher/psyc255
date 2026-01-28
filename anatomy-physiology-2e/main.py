from getFiles import list_files_pathlib, list_all_files_os_walk
from createMenu import createTex,cleanedTitle
from convert import slideConvert, wordConvert

def main():
    textbook = list_files_pathlib('anatomy-and-physiology-2e')
    # slides = list_files_pathlib('slides')
    label = list_all_files_os_walk('label_images')
    
    # createTex("textbook.tex",textbook)
    # slideConvert('slides', 'slide_pdf')
    # createTex("label_image.tex", label)
    title = r"anatomy-physiology-2e/anatomy-and-physiology-2e/28-review-questions.docx"
    cleanedTitle(title)

        
        
        


if __name__=="__main__":
    main()