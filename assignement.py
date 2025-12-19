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
def Igala() :
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
word = input('Enter your english word : ')
print(d[word]) 

print('Welcome to your dictionary')
print(1 = "french") 
print(2 = "Igala") 
Choice = int(input('Please enter the number for your language : '))
if Choice == 1 : 
    french_dict()
elif Choice == 2 : 
    Igala_dict()
else :
print ('Language not found')



