import tkinter as tk
from tkinter import filedialog, messagebox
from arabicpy import transpile_file
import os

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("ArabicPy files", "*.pyar")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def convert():
    file_path = entry_file_path.get()
    if not file_path or not file_path.endswith(".pyar"):
        messagebox.showerror("خطأ", "الرجاء اختيار ملف بصيغة .pyar")
        return

    try:
        transpile_file(file_path)
        messagebox.showinfo("نجاح", f"تم التحويل! الملف محفوظ في مجلد build/")
    except Exception as e:
        messagebox.showerror("فشل", f"حدث خطأ أثناء التحويل:\n{e}")

# نافذة GUI
root = tk.Tk()
root.title("ArabicPy GUI")

tk.Label(root, text="اختر ملف .pyar لتحويله:").pack(pady=5)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.pack(padx=10)

tk.Button(root, text="استعراض", command=choose_file).pack(pady=5)
tk.Button(root, text="تحويل", command=convert, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
