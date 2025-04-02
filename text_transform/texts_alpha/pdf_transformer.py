import os
from pdfminer.high_level import extract_text
import time

def extract_text_from_pdf(pdf_path, TEXT):
    with open(pdf_path, 'rb') as pdf_file:
        text  = extract_text(pdf_file)
        TEXT += text
    return TEXT


if  __name__ == '__main__':

    pdf_file_path   = "native\pdfs"
    ext             = ('.pdf')
    txt_file_path   = '..\\texts_txt\\native\\N_PDF_CORPUS.txt'
    TEXT_result    = '' #this starts off the chain
    debug_counter   = 0
    
    start_time = time.time()
    print("--- starting pdf transformer ---")
    for files in os.listdir(pdf_file_path):
        if files.endswith(ext):
            target_file = f"native\\pdfs\\{files}"
            TEXT_result = extract_text_from_pdf(target_file, TEXT_result)
            debug_counter   += 1
        else:
            continue
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(TEXT_result)
    print(f"PDFs converted: {debug_counter}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"DONE: Elapsed time: {elapsed_time} sec")

    