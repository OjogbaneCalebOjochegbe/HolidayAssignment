import tkinter as tk
from tkinter import ttk

# Yoruba dictionary (English to Yoruba)
Yoruba_dictionary = { 
    'hello': 'pele o',
    'come': 'wa',
    'go': 'lo',
    'stay': 'duro',
    'here': 'nibi',
    'near': 'nitosi',
    'far': 'ji na',
    'happy': 'dun',
    'sad': 'ibanuje',
    'filled': 'kun',
    'hungry': 'ebi npa',
    'money': 'owo',
    'please': 'jowo',
    'name': 'oruko',
    'food': 'onje',
    'sorry': 'ma binu',
    'love': 'ife',
    'what': 'kini?',
    'thank you': 'o se',
    'congratulations': 'ku oriire'
}

def search_word():
    """
    Searches for the Yoruba translation of the entered English word and updates the result label.
    """
    word = word_entry.get().lower()
    translation = Yoruba_dictionary.get(word)

    if translation:
        result_label.config(text=f"{word} : {translation}")
    else:
        result_label.config(text="Word not found, click the 'Show the available words' button")

def show_words():
    """
    Displays the words available in the dictionary.
    """
    words_listbox.delete(0, tk.END)
    for word in Yoruba_dictionary.keys():
        words_listbox.insert(tk.END, word)

# App begins
root = tk.Tk()
root.geometry("600x250")
root.title("Yoruba Dictionary")

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