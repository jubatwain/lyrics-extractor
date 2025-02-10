import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import io


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    extract_text(file_path)


def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Basic cleaning for lyrics extraction (you might need to adjust this)
    lines = text.split('\n')
    lyrics = [line.strip() for line in lines if line.strip()]

    result_text.delete(1.0, tk.END)  # Clear previous text
    result_text.insert(tk.END, '\n'.join(lyrics))


# Set up the main window
root = tk.Tk()
root.title("PDF Lyrics Extractor")

# Button to select PDF
select_button = tk.Button(root, text="Select PDF", command=select_file)
select_button.pack(pady=10)

# Text widget to display results
result_text = tk.Text(root, wrap=tk.WORD, height=20, width=50)
result_text.pack(padx=10, pady=10)

# Start the GUI
root.mainloop()