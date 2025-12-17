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
    print('Language not found')   