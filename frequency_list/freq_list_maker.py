import csv
#check encoding
from chardet.universaldetector import UniversalDetector

'''
Turns the list of most frequent lemmas, according to 
Serge Sharoff, and turns the .num file into
.csv file
'''

detector = UniversalDetector()

with open('5000lemma.num', 'rb') as file:
    for line in file:
        detector.feed(line)
        if detector.done:
            break
    detector.close()

encoding = detector.result['encoding']

print(f"List encoding: {encoding}")

file_path   = '5000lemma.num'  # Replace with your file path (other frequency lists are available)
output_path = 'verbs_Freqlist_scrape.csv'  # Replace with your desired output file path


with open(file_path, 'r', encoding='windows-1251') as file, open(output_path, 'w', newline='', encoding='windows-1251') as output_file:
    reader = csv.reader(file, delimiter=' ')  # delimited by tabs in original list
    writer = csv.writer(output_file)

    writer.writerow(['Lemma', 'WordType'])

    next(reader, None)

    for row in reader:
        if row:
            rank, frequency, lemma, word_type = row
            
            if word_type.lower() == 'verb':
                writer.writerow([lemma, word_type])

