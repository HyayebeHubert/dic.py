def french_dict():
    d = {
        'House' : 'Maison',
        'Book' : 'Livre',
        'Water' : 'Eau',
        'Sun' : 'Soleil',
        'Food' : 'Nourriture',
        'Dog' : 'Chien',
        'Cat' : 'Chat',
        'Car' : 'Voiture',
        'Tree' : 'Arbre',
        'Road' : 'Route',
        'School' : 'Ecole',
        'Friend' : 'Ami',
        'Phone' : 'Telephone',
        'Chair' : 'Chaise',
        'Table' : 'Table',
        'Light' : 'Lumiere',
        'Child' : 'Enfant',
        'Work' : 'Travail',
        'Love' : 'Amour',
        'Music' : 'Musique',
    }     
    word = input('Enter your english word : ')
    print(d[word]) 
print('Welcome to your dictionary')
print()
Choice = int(input('Please enter the number for your language : '))
if Choice == 1 : 
    french_dict()
else : 
print ('Language not found')
       words = {
    "come": "ya",
    "stand": "de",
    "sit": "kpe",
    "god": "ojo",
    "morning": "okpo",
    "night": "oche",
    "we/us": "enye",
    "water": "omi",
    "drink": "mu",
    "leave": "lo",
    "understand": "ma",
    "how": "ele",
    "long time": "akpa kpekpe",
    "school": "sukulu",
    "take": "re",
    "tomorrow": "ojo ale",
    "write": "kwo",
    "car": "moto",
    "how was your day": "ele ne ojo che",
    "did you sleep well": "ma kpe chọ",
    "yes": "ee",
    "i want": "mi fẹ",
    "everything": "ogbogbo",
    "mother": "iya"
}

print("Translate Words from English to Igala")
print("Choose a word from the list below:\n")

for word in words:
    print("--", word)

while True:
    word = input("\nEnter word to be translated: ").lower()

    if word in words:
        print(f"'{word}' means '{words[word]}'")
        break
    else:
        print(f"Sorry, '{word}' is not in the dictionary. Try again.") 11
