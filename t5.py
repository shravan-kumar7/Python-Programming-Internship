import tkinter as tk
from tkinter import messagebox, filedialog

def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(reversed(text.split()))

def process_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Input Error", "Please enter some text.")
        return
    
    if reversal_type.get() == "char":
        result = reverse_characters(text)
    else:
        result = reverse_words(text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def save_to_file():
    result = output_text.get("1.0", tk.END).strip()
    if not result:
        messagebox.showerror("Save Error", "There is no text to save.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(result)
        messagebox.showinfo("Saved", f"Text saved to {file_path}")

# GUI Setup
root = tk.Tk()
root.title("Text Reverser")

# Input Frame
tk.Label(root, text="Enter text:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)

# Reversal Options
reversal_type = tk.StringVar(value="char")
tk.Radiobutton(root, text="Reverse Characters", variable=reversal_type, value="char").pack(anchor="w")
tk.Radiobutton(root, text="Reverse Words", variable=reversal_type, value="word").pack(anchor="w")

# Action Buttons
tk.Button(root, text="Reverse", command=process_text).pack(pady=5)

# Output Frame
tk.Label(root, text="Reversed text:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

tk.Button(root, text="Save to File", command=save_to_file).pack(pady=5)

root.mainloop()
