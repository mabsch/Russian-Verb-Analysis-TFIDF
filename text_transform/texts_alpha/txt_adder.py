import os
import time

def TXT_adder(txt_path, TEXT):
    with open(txt_path, 'r', encoding='UTF-8') as txt_file:
        text = txt_file.read()
    TEXT += text
    return TEXT


if  __name__ == '__main__':

    txt_file_path           = "nonnative\\txts"
    ext                     = ('.txt')
    TOTAL_txt_file_path     = r'..\texts_txt\nonnative\NN_TOTAL_CORPUS.txt'
    TEXT_result             = '' #this starts off the chain

    debug_counter   = 0
    
    start_time = time.time()
    print("--- starting txt adder ---")
    for files in os.listdir(txt_file_path):
        if files.endswith(ext):
            target_file = f"{txt_file_path}\\{files}"
            TEXT_result = TXT_adder(target_file, TEXT_result)
            debug_counter   += 1
        else:
            continue
    with open(TOTAL_txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(TEXT_result)
    print(f"TXTs added: {debug_counter}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"DONE: Elapsed time: {elapsed_time} sec")    