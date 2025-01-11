import tkinter as tk
from tkinter import ttk

# Spanish dictionary (English to Spanish)
spanish_dictionary = { 
    'hello': 'hola',
    'come': 'venir',
    'go': 'ir',
    'stay': 'permanecer',
    'apple': 'manzana',
    'water': 'agua',
    'milk': 'leche',
    'happy': 'feliz',
    'boy': 'el niño',
    'girl': 'la niña',
    'hungry': 'hambriento',
    'money': 'el dinero',
    'please': 'por favor',
    'good night': 'buenas noches',
    'good morning': 'buenos días',
    'sorry': 'lo siento',
    'love': 'amar',
    'restaurant': 'restaurante',
    'thank you': 'gracias',
    'clothes': 'la ropa'
}

def search_word():
    # Searches for the Spanish translation of the entered English word and updates the result label.
    word = word_entry.get().lower()
    translation = spanish_dictionary.get(word)

    if translation:
        result_label.config(text=f"{word} : {translation}")
    else:
        result_label.config(text="Word not found, click the 'Show the available words' button")

def show_words():
    # Displays the words available in the dictionary.
    words_listbox.delete(0, tk.END)
    for word in spanish_dictionary.keys():
        words_listbox.insert(tk.END, word)

# App begins
root = tk.Tk()
root.geometry("600x250")
root.title("Spanish Dictionary")

word_entry = tk.Entry(root)
word_entry.pack()

search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

words_listbox = tk.Listbox(root)
words_listbox.pack()

show_button = tk.Button(root, text="Show the available words", command=show_words)
show_button.pack()

root.mainloop()