# Russian-Verb-Analysis-TFIDF
A project I developed at KazNU analyzing verb usage by different groups in Russian. This is an initial proof of concept, which was accompanied by a presentation to a large audience of Russian speakers.

 ## Background

Correct Russian verb usage is one of the most difficult aspects of learning the language. The complexities of Russian verbs arise from multiple factors, which include but are not restricted to: verbal aspect, conjugation patterns, semantic changes by case, and case agreement...

This project was developed during the second half of my Flagship Capstone year in Kazakhstan, where I focused on creating an analytical approach to diagnose any irregular verb usage, and create planes to encourage more standard language.

## Theoretical Framework

From anecdotal experience, a frequent observation in the Russian language skills of Americans, is the overusage of specific verbs, which affects speech patterns, and discourages the use of certain grammatical structures. For example, while the verb **быть (to be)** is omitted in the present tense, American students tend to use verbs that bypass this grammatical structure (являться is the identified overused verb). The results from this analysis supports this, as other verbs such as иметь are used to by-pass the verb *to have*, which is not necessarily present in the speech of native speakers. One of the issues this poses lies in the fact that these overused verbs typically rely on grammatical structures found in higher registers of the language, causing a disconnect from effective communication.  

Due to this fact, I argue that a lack of vocabulary impedes students from using the appropriate grammatical structures, and not necessarily a lack of understanding of Russian grammar. The incorrect conjugation of verbs could also keep students from using their prior knowledge of verbs, in novel situations, which would present itself as a defficiency in spontaneous speech generation, which is tested for under [ILR](https://govtilr.org) standards.

To test this idea, I implemented a system to gather all verbs in three collections of texts in Russian, and classify them into the 16 categories described by the Russian linguist [Andrey Zalisniak](https://en.wiktionary.org/wiki/Appendix:Russian_verbs#Classification). This is novel, in the sense that typically students of Russian in the USA will often only learn a classification with 2 main categories, which vastly oversimplifies an understanding of verb usage and proper conjugation.

## Methods

I used the list of most common lemmas, according to [Serge Sharoff](https://www.artint.ru/projects/frqlist/frqlist-en.php), to define the verbs of interest. Then, I compiled two sets of texts, one from native Russian speakers, and the second from non-native speakers--all mostly sourced from students at KazNU. I processed all the texts into a single file format, and began extracting all the verbs, organizing them by their infinitive form, and tallying their counts. Once all the data was collected, I wrote an implementation of the *TF-IDF* measure of importance, and assigned scores to the verb usage by each group, for comparison. Three groups are identified, the Russian corpus (in the form of a frequency list), Non-Native students, and Native students.

Further steps taken in this project, but not included in the report, entail scraping the ID numbers for each verb, according to Wiktionary, to access article information. The choice to keep all data in the structre detailed earlier, is from the necessity to make personalized Anki flashcards for the students in the non-native speaker group. By referring to all instances of a verb by its infinitive form, important details can be drawn from its Wiktionary article, such as: translation, definition, case agreement, all conjugated forms, etc.. 

The code for the Anki deck generator is also included in this repository and uses the [Genanki library](https://github.com/kerrickstaley/genanki). The webscraping portion is also included, and any modifications should continue to abide the usage guidelines of the [Wiktionary api](https://en.wiktionary.org/w/api.php), any data obtained from Wiktionary articles must adhere the [friendly bot guidelines](https://en.wiktionary.org/robots.txt), and must be done under no commercial usage.

## Future Steps

Broadening the scope of this project would require a larger amount of non-native and native data, for a better comparison with the Russian corpus of texts, as the current results cannot ascertain unstandard verb usage, when the differences between groups are small (not statistically significant). Once more data is obtained, other possible NLP techniques could be implemented, for example a pretrained [Spacy](https://github.com/explosion/spaCy) pipeline could be incorporated into the workflow, to identify the usage of other lemmas (where adjectives could prove to be of particular interest). A possible standardization of the data structure, sacrificing the Wiktionary data, could streamline the process for analysis, incorporating pre-built measurement metrics, or ML approaches, such as those found in the [Scikit-learn library](https://scikit-learn.org/stable/index.html).

I would also like to collaborate with educators in different regions to further expand on the pedagogical implications of this study, and produce useful strategies to improve language acquisition techniques. I have also included a [Russian draft of my report](Классификация_и_преподавание_русских_глаголов.pdf) detailing the first iteration of this project.