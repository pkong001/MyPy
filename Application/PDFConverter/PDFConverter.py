import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        """GUI"""
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("400x200")

        self.instruction_label = tk.Label(root, text="To sort-merge order, please rename the PDF files (ascending).",
                                          wraplength=350, justify="center", fg="blue")
        self.instruction_label.pack(pady=10)

        self.btn_merge = tk.Button(root, text="Select Fucking Folder", command=self.merge_pdfs)
        self.btn_merge.pack(pady=20)

    def merge_pdfs(self):
        """process."""
        folder_selected = filedialog.askdirectory(title="Select Folder Containing PDFs")
        if not folder_selected:
            return

        pdf_files = sorted(
            [os.path.join(folder_selected, f) for f in os.listdir(folder_selected) if f.endswith(".pdf")]
        )

        if not pdf_files:
            messagebox.showwarning("Warning", "No PDF files found in the selected folder.")
            return

        output_name = filedialog.asksaveasfilename(title="Save Merged PDF As", defaultextension=".pdf",
                                                   filetypes=[("PDF Files", "*.pdf")])

        if not output_name:
            return

        # Disable the button while processing
        self.btn_merge.config(state="disabled")

        try:
            # Merge PDFs
            merger = PdfMerger()
            for pdf in pdf_files:
                merger.append(pdf)

            merger.write(output_name)
            merger.close()

            messagebox.showinfo("Success", f"Merged and saved:\n{output_name}")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

        finally:
            # Re-enable button after processing
            self.btn_merge.config(state="normal")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
