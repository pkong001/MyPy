import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs():
    folder_selected = filedialog.askdirectory(title="Select Folder Containing PDFs")
    if not folder_selected:
        return

    # Get all PDF files in the selected folder
    pdf_files = [os.path.join(folder_selected, f) for f in os.listdir (folder_selected) if f.endswith(".pdf")]


    output_name = filedialog.asksaveasfilename(title="Save Merged PDF As", defaultextension=".pdf",
                                               filetypes=[("PDF Files", "*.pdf")])

    if not output_name:
        return

    # Merge PDFs
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_name)
    merger.close()

    messagebox.showinfo("Success", f"PDFs merged and saved as:\n{output_name}")

# Create GUI
root = tk.Tk()
root.title("PDF Merger")
root.geometry("300x150")

instruction_label = tk.Label(root, text="To sort-merge order, please rename the PDF files (ascending).", wraplength=300, justify="center", fg="blue")
instruction_label.pack(pady=10)

btn_merge = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
btn_merge.pack(pady=20)

root.mainloop()
