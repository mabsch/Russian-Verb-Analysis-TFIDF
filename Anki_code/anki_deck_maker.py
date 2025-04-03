import pandas as pd
import genanki

'''
This script takes Anki Dictionaries and turns them into Anki Decks.
For each new Anki Deck, you MUST change the df below, AND hardcode a new
Deck ID. Otherwise, Anki will overwrite your decks, once imported. 
'''

df      = pd.read_csv('Anki_Dict_class 10.csv') # Other example decks included

###style

style = '''
/* Default styles for light mode */
.card {
    font-family: 'Times New Roman', sans-serif;
    font-size: 30px;
    text-align: center;
    color: #000;  /* Valid color value */
    background: linear-gradient(76deg, rgba(255, 243, 248, 0.7) 50%, rgba(238, 246, 255, 0.7) 100%),
                url("C:/Users/Angel/Pictures/_backgrounds/tarkostill.jpg");  /* Ensure the URL path is correct */
    background-size: cover;  /* Ensure the background covers the card */
    background-repeat: no-repeat;  /* Prevent background repetition */
    background-position: center;  /* Center the background image */
}

/* Dark mode styles */
@media (prefers-color-scheme: dark) {
    .card {
        color: #fff;  /* Change text color for dark mode */
        background: linear-gradient(76deg, rgba(0, 0, 0, 0.7) 50%, rgba(48, 48, 48, 0.7) 100%),
                    url("C:/Users/Angel/Pictures/_backgrounds/tarkostill.jpg");  /* Ensure the URL path is correct */
        background-size: cover;  /* Ensure the background covers the card */
        background-repeat: no-repeat;  /* Prevent background repetition */
        background-position: center;  /* Center the background image */
    }
    .spoiler span {
        color: #fff;
    }
}

.spoiler {
    cursor: pointer;
    color: #8b74f2;
}

.spoiler span {
    display: none;
    color: black;
}

.spoiler:hover span {
    display: inline;
}

.center {
    margin: auto;
    width: 60%;
    border: 3px solid #73AD21;
    padding: 10px;
    text-align: left;
    font-size: 25px;
}

'''


my_model = genanki.Model(
  1670239,
  'Simple Model',
  fields=[
    {'name': 'WORDS'},
    {'name': 'DEFINITIONS'},
    {'name': 'CONJUGATIONS'}
    ],
  templates=[
{
    'name': 'Card 1',
    'qfmt': """
        <div class="question">
            <span class="word">{{WORDS}}</span>
            <br><br>
            <div class="timer" id="s2"></div>
            <script>
                function countdown(elementName, minutes, seconds) {
                    var element, endTime, hours, mins, msLeft, time;

                    function twoDigits(n) {
                        return (n <= 9 ? "0" + n : n);
                    }

                    function updateTimer() {
                        msLeft = endTime - (+new Date);
                        if (msLeft < 1000) {
                            element.innerHTML = "!!!!!!!!!!";
                        } else {
                            time = new Date(msLeft);
                            hours = time.getUTCHours();
                            mins = time.getUTCMinutes();
                            element.innerHTML = (hours ? hours + ':' + twoDigits(mins) : mins) + ':' + twoDigits(time.getUTCSeconds());
                            setTimeout(updateTimer, time.getUTCMilliseconds() + 500);
                        }
                    }

                    element = document.getElementById(elementName);
                    endTime = (+new Date) + 1000 * (60 * minutes + seconds) + 500;
                    updateTimer();
                }

                countdown("s2", 0, 5);  // 2nd value is the minute, 3rd is the seconds
            </script>
        </div>
    """,

    'afmt': """
        <div class="answer">
            <span class="word">{{WORDS}}</span>
            <br>
            <br>
            <span class="definition">{{DEFINITIONS}}</span>
            <br>
            <br>
            <div class="spoiler">
                <hr class="divider">
                <span class="conjugations">{{CONJUGATIONS}}</span>
            </div>
        </div>
    """,

    'css': style
}], css=style)

###

Deck_ID = 1104592 #hard code this
'''
For the sake of reproducibility:
run in terminal
>>python
>>import random
>>print(random.randrange(1 << 30, 1 << 31)) 
I understand all this can be incorporated to the script, 
but not everyone is familiar with importing decks.
'''

symbols_to_remove = ["[", "]", "'", "\\n"]
def remove_symbols(text):
    for symbol in symbols_to_remove:
        text = text.replace(symbol, "")
    return text

df_cleaned = df.applymap(remove_symbols)
Verb_Category = "class 10 verbs"

my_deck = genanki.Deck(Deck_ID,Verb_Category) #have to hard code the ID
for _, row in df_cleaned.iterrows():
    # Here, _ is the index (which is not used), and row is the Pandas Series representing the row data
    card = genanki.Note(
        model=my_model,
        fields=[row['WORDS'], row['DEFINITIONS'], row['CONJUGATIONS']]
    )
    my_deck.add_note(card)


file_path = '..\\frequency_list\\Anki_code'
genanki.Package(my_deck).write_to_file(f'{file_path}\Anki_{Verb_Category}.apkg')

# example deck included for viewing