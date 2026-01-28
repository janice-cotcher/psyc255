def createTex(name,files):
    header = """
\\documentclass{book}
\\usepackage{enumitem}
\\usepackage{xcolor}
\\usepackage[colorlinks=true, linkcolor=blue, urlcolor=blue]{hyperref}
\\author{}
\\date{}
\\title
\\begin{document}
\\maketitle
\\tableofcontents
    """
    footer = """
[Title of Work]" by OpenStax, Rice University is licensed under CC BY 4.0. This is a modified version of the original work. Available at \\url{https://openstax.org/details/books/anatomy-and-physiology-2e}
\\end{document}
"""
    with open(name, "w") as output:
        output.write(header)
        
        for file in files:
            output.write(f"\\section{file}")
        output.write(footer)
    print(f"{name} was successfully created")