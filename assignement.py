import streamlit as st
french = {
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

Igala = {
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

yoruba = {
    "water": "omi",
    "food": "ounje",
    "house": "ile",
    "man": "okunrin",
    "woman": "obinrin",
    "child": "omo",
    "book": "iwe",
    "school": "ile-iwe",
    "sun": "oorun",
    "moon": "osupa",
    "dog": "aja",
    "cat": "ologbo",
    "road": "ona",
    "car": "oko ayokele",
    "money": "owo",
    "friend": "ore",
    "love": "ife",
    "day": "ojo",
    "night": "oru",
    "teacher": "oluko"
}

hausa = {
    "chair": "kujera"
    "stone": "dutse"
    "bag": "jaka"
    "shoe": "takalmi"
    "wrapper": "zani"
    "phone": "waya"
    "bed": "godo"
    "food": "abichin"
    "clothes": "kaya"
    "plates": "kwanu"
    "bottle": "gora" 
    "scissors": "almakachi"
    "knife": "wuka"
    "basket": "kwondo"
    "house": "Gida"
    "money": "kudi" 
    "car": "mota"
    "water": "ruwa"
    "horse": "doki"
    "bone': "Kashi"
choice = st.selectbox9('language',('french','Igala','yoruba', 'hausa',))
def search_dictionary(word, dictionary):
    return dictionary[word]

if choice == 'french':
    dictionary = french
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
 elif choice == 'Igala':
    dictionary = Igala
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
 elif choice == 'yoruba':
    dictionary = yoruba
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
 elif choice == 'hausa':
    dictionary = hausa
    your_word = st.text_input('Enter Your word: ')
    st.button('search', on_click = lambda:
     st.title(search_dictionary(your_word.lower(), dictionary)))
