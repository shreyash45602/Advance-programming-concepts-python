import os
import PyPDF2
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()

pdf = filedialog.askopenfilenames(
    title="Select PDF files",
    filetypes=[("PDF Files", "*.pdf")]
)

merge = PyPDF2.PdfMerger()

for file in pdf:
    merge.append(file)

merge.write("merge.pdf")
merge.close()

print("PDF merged successfully!")