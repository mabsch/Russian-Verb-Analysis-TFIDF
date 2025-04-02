import os
import numpy as np
import re
from collections import Counter

def verb_filter(count_arr, conjs_df, all_conjs_arr):
    for i in count_arr:
        for idx, df in enumerate(conjs_df):
            if i[0] in df.values:
                matched_conj = df.index[df.isin([i[0]]).any(axis=1)].tolist()
                conj_idx = np.where(matched_conj == all_conjs_arr[:, 0])[0][0]
                if conj_idx:  # or if len(conj_idx) > 0:
                    all_conjs_arr[conj_idx, 1]     += i[1]
                    all_conjs_arr[conj_idx, 2]      = f'Class {idx + 1}'
                    
    NonZ_all_conjs = all_conjs_arr[all_conjs_arr[:, 1] != 0]
    return NonZ_all_conjs

def doc_counter(file_path):
    with open(file_path, encoding='utf-8') as file:
        words = re.findall(r'\w+', file.read().lower())

    top_words_test = Counter(words)
    c_list_test    = list(top_words_test.items())

    c_arr_test  = np.array(c_list_test, dtype=object)
    total_doc_words = np.sum(c_arr_test[:,1])
    return c_arr_test, total_doc_words


def TFIDF_counter(file_path, corpus_arr, conjs_df, all_conjs_arr):
    '''
    Calculates TF-IDF scores for all verbs in the corpus.
    Generates a test array for each doc, comparing to the whole
    Input:
    file_path   - directory with individual documents of the corpus
    corpus_arr  - array with the total counts of the corpus
                  in a single array.
    Returns:
    TFs_N - np.array of lists, where the lists contain ind. TF scores
    IDF_N - np.array with the log(IDF) score for the word in the corpus
    '''
    TFs_N      = np.empty(len(corpus_arr), dtype=object)
    TFs_sum    = np.empty(len(corpus_arr), dtype=int)
    for i in range(np.size(TFs_N)):
        TFs_N[i] = []
    finds_N    = np.zeros(len(corpus_arr))
    IDF_N      = np.zeros(len(corpus_arr))

    for count, files in enumerate(os.listdir(file_path)):
        if files.endswith('.txt'):
            c_arr, total_words = doc_counter(f'{file_path}\\{files}')
            #Important, it's getting the non-zero counts
            c_arr = verb_filter(c_arr, conjs_df, all_conjs_arr)
            for i in c_arr:
                w_check = np.where(i[0] == corpus_arr)[0]
                if w_check.size>0:
                    TF = i[1] / total_words
                    TFs_N[w_check[0]].append(TF)
                    finds_N[w_check[0]] += 1
                else:
                    pass
    doctotal = count + 1
    for idx in range(len(corpus_arr)):
        if finds_N[idx] != 0:
            IDF_N[idx] = np.log10((1 + doctotal) / (finds_N[idx] + 1)) + 1#smooth
        else:
            # Handle the case when finds_N[idx] is zero
            # This is fine, bc TF * IDF == 0
            IDF_N[idx] = 0
    for idx, TF_list in enumerate(TFs_N):
        TF_sum       = sum(TF_list)
        TFs_sum[idx] = TF_sum
    TF_IDF = TFs_sum * IDF_N
    norm   = np.linalg.norm(TF_IDF)
    Norm_TF_IDF = TF_IDF/norm

    return Norm_TF_IDF