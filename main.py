import tkinter as tk
def reverse_text():
    text = entry.get()
    reversed_text = text[::-1]
    result_label.config(text="Аударылған сөз: " + reversed_text)
root = tk.Tk()
root.title("Сөз аудару программа")

num = tk.Label(root, text="Программа пайдалану", font=("Arial", 16, "bold"))
num.pack()

num_description = tk.Label(root, text="Сөзді жазыңыз және 'Аудару' түймесін басыңыз:")
num_description.pack()
entry = tk.Entry(root)
entry.pack()

reverse_button = tk.Button(root, text="Аудару", command=reverse_text)
reverse_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()