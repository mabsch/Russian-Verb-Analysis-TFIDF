# Using the text_transform folder

Here I have included all the original documents collected from the different groups, i.e. class curricula, native speakers, non-native speakers.
This folder serves as the data, which [tfidf.py](tfidf.py) runs over to compare to the obtained words in **..\frequency_list**. For the sake of consistency, I have included functions that turn doc, docx, and pdf files into a txt file, and creates a single documents, which are later parsed. 

The main analysis of the data is done under [verb_analytics.ipynb](verb_analytics.ipynb). Only consider modifying **\texts_alpha** if you wish to incorporate new data.