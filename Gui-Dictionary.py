import json
import tkinter as tk

root = tk.Tk()
root.title("Dictionary")
root.minsize(400,200)
root.maxsize(1000,200)

input_label = tk.Label(root, text = "Enter the word you want to find : ")
input_label.pack()

input_entry = tk.Entry(root, text = "Enter here ")
input_entry.pack()

def search():
    with open("data.json") as data:
        dic = data.read()
    j = json.loads(dic)

    user_input = input_entry.get()

    for i in j[user_input]:
        output_label = tk.Label(root, text = i)
        output_label.pack()

submitbutton = tk.Button(root, text = "Search", command = search)
submitbutton.pack()


root.mainloop()