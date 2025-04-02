import docx2txt
import os
import time

def extract_text_from_docx(docx_path, TEXT):
    with open(docx_path, 'rb') as docx_file:
        text = docx2txt.process(docx_file)
        TEXT += text
    return TEXT


if  __name__ == '__main__':

    docx_file_path   = "class"
    ext             = ('.docx')
    txt_file_path   = '..\\texts_txt\\class\\C_DOCX_CORPUS.txt'
    TEXT_result    = '' #this starts off the chain
    debug_counter   = 0
    
    start_time = time.time()
    print("--- starting docx transformer ---")
    for files in os.listdir(docx_file_path):
        if files.endswith(ext):
            target_file = f"class\\{files}"
            TEXT_result = extract_text_from_docx(target_file, TEXT_result)
            debug_counter   += 1
        else:
            continue
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(TEXT_result)
    print(f"DOCXs converted: {debug_counter}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"DONE: Elapsed time: {elapsed_time} sec")

    