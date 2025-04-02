import csv
import ast
import time

def read_scraped_verbs(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        return [row for row in reader]
    

def save_verb_dicts(File_Name, Verb_Dict):

    # Write the dictionary to a CSV file
    with open(f'Anki_Dict_{File_Name}.csv', 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["WORDS", "DEFINITIONS", "CONJUGATIONS"])
        
        # Write data
        for row in zip(Verb_Dict["WORDS"], Verb_Dict["DEFINITIONS"], Verb_Dict["CONJUGATIONS"]):
            csv_writer.writerow(row)


if __name__ == '__main__':
    Scraped_verbs = ['class 9','class 10',
                'class 11','class 12',
                'class 13','class 14',
                'class 15','class 16',
                'irregular']
    
    for s_class in Scraped_verbs:
        start_time = time.time()
        scraped_verbs = read_scraped_verbs(f'..\\Scraped_verbs_{s_class}.csv')

        words           = []
        definitions     = []
        conjugations    = []

        for i in scraped_verbs:
            rw0 = ast.literal_eval(i[0])
            words.append(rw0[0:2])
            definitions.append(rw0[2:])

            rw1 = ast.literal_eval(i[1])
            conjugations.append(rw1)

        verb_dict = {"WORDS": words, 
                    "DEFINITIONS" : definitions, 
                    "CONJUGATIONS": conjugations}
        save_verb_dicts(s_class, verb_dict)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} sec")
