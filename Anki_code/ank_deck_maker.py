import pandas as pd
import genanki

###word source
"""
We need to get the words in, such that the dataframe is created in an
appropriate way to feed into the loop. Notice the need for strings. Notice
the need to transpose. Notice the dataframe to a dictionary
"""
base = {}
russ_df = pd.read_excel(r'C:\Users\Angel\Documents\Russ\flagship\pandatest.xlsx')
russ_df = russ_df.applymap(str)
temp = russ_df.transpose()
base = temp.to_dict()
print(base.keys())

###style
"""
this is design stuff from deck builder py
"""

style = """
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
"""

"""
This lays out how the cards will exist, and creates a deck. Notice the need to
hardcode id numbers into the decks
"""

my_model = genanki.Model(
  1670239391,
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
                            element.innerHTML = "Го!";
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

    'css': """
        .card {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
            text-align: center;
            color: #333;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            padding: 20px;
        }

        .question {
            font-weight: bold;
        }

        .word {
            font-size: 24px;
        }

        .timer {
            font-size: 20px;
            color: red;
        }

        .answer {
            font-weight: bold;
        }

        .definition {
            text-decoration: underline;
        }

        .spoiler {
            color: gray;
            margin-top: 20px;
        }

        .spoiler hr.divider {
            border: 0;
            height: 1px;
            background: #ccc;
        }

        .conjugations {
            font-style: italic;
        }
    """
}

  ],
    css = style)

###
"""
This is the loop that eats up the previous dictionary
"""
Deck_ID = 336897098
Verb_Category = "---"

my_deck = genanki.Deck(Deck_ID,Verb_Category) #have to hard code the ID
for i in base.keys():
    entry = base[i]
    print(entry)
    card = genanki.Note(
    model = my_model,
    fields =[entry['WORDS'],
             entry['DEFINITIONS'],
             entry['CONJUGATIONS']])

    my_deck.add_note(card)

file_path = 'C:\\Users\\Angel\\Dropbox\\My PC (UNC-PF2A4YMK)\\Documents\\Capstone\\frequency_list\\Anki_code'
genanki.Package(my_deck).write_to_file(f'{file_path}\{Verb_Category}.apkg')
