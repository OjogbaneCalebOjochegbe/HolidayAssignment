import tkinter as tk

# Japanese dictionary (English to Japanese in romaji)
japanese_dictionary = {
    'hello': 'konnichiwa',
    'come': 'kuru',
    'go': 'iku',
    'stay': 'tomeru',
    'apple': 'ringo',
    'water': 'mizu',
    'milk': 'miruku',
    'happy': 'shiawase',
    'boy': 'otokonoko',
    'girl': 'onnanoko',
    'hungry': 'onaka suita',gr
    'money': 'okane',
    'please': 'onegai',
    'good night': 'oyasumi',
    'good morning': 'ohayou',
    'sorry': 'gomen',
    'love': 'ai',
    'restaurant': 'resutoran',
    'thank you': 'arigatou',
    'clothes': 'fuku'
}

def search_word():
    # Searches for the Japanese translation of the entered English word and updates the result label.
    word = word_entry.get().lower()
    translation = japanese_dictionary.get(word)

    if translation:
        result_label.config(text=f"{word} : {translation}")
    else:
        result_label.config(text="Word not found, click the 'Show the available words' button")

def show_words():
    # Displays the words available in the dictionary.
    words_listbox.delete(0, tk.END)
    for word in japanese_dictionary.keys():
        words_listbox.insert(tk.END, word)

# App begins
root = tk.Tk()
root.geometry("600x250")
root.title("Japanese Dictionary")

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