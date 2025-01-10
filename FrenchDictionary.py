import tkinter as tk
from tkinter import ttk

# French dictionary (English to French)
French_dictionary = { 
    'hello': 'salut',
    'come': 'viens',
    'go': 'aller',
    'stay': 'rester',
    'here': 'ici',
    'near': 'près',
    'far': 'loin',
    'happy': 'heureux',
    'sad': 'triste',
    'filled': 'rempli',
    'hungry': 'affamé',
    'money': 'argent',
    'please': 'sil vous plaît',
    'name': 'nom',
    'food': 'nourriture',
    'sorry': 'désolé',
    'love': 'amour',
    'what': 'que',
    'thank you': 'merci',
    'congratulations': 'félicitations'
}

def search_word():
    # Searches for the French translation of the entered English word and updates the result label.
    word = word_entry.get().lower()
    translation = French_dictionary.get(word)

    if translation:
        result_label.config(text=f"{word} : {translation}")
    else:
        result_label.config(text="Word not found, click the 'Show the available words' button")

def show_words():
    # Displays the words available in the dictionary.
    words_listbox.delete(0, tk.END)
    for word in French_dictionary.keys():
        words_listbox.insert(tk.END, word)

# App begins
root = tk.Tk()
root.geometry("600x250")
root.title("French Dictionary")

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