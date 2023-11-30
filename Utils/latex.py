import fitz  # PyMuPDF
import re
import tabula

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def extract_tables_from_pdf(pdf_path):
   
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

def clean_and_escape(text):
    
    text = text.replace('&', '\\&').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_').replace('$', '\\$')

    
    text = text.replace('\n', '\\newline\n')

    return text

def generate_latex(text, tables):
    cleaned_text = clean_and_escape(text)

    
    table_content = ""
    for i, table in enumerate(tables):
        table_content += f"\\textbf{{Table {i + 1}:}}\n{table.to_latex(index=False)}\n"

    
    latex_content = r"""
    \documentclass{article}
    \begin{document}
    %s

    %s
    \end{document}
    """ % (cleaned_text, table_content)

    return latex_content

def save_latex(latex_content, output_file):
    with open(output_file, 'w') as f:
        f.write(latex_content)


pdf_path ='/Users/sermadkarim/Documents/Project/Proj/Mark-scheme-Paper-1-Financial-accounting-June-2022.pdf'
output_file = "output1.tex"

text_data = extract_text_from_pdf(pdf_path)
tables_data = extract_tables_from_pdf(pdf_path)

latex_content = generate_latex(text_data, tables_data)
save_latex(latex_content, output_file)