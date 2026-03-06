import tkinter as tk
from tkinter import messagebox
import os
import sys
import pyperclip

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def run_test():
    try:
        # 1. Test Clipboard
        pyperclip.copy("CLIPBOARD_SUCCESS")
        
        # 2. Test File Writing (Memory)
        log_path = os.path.join(get_base_path(), "test_log.txt")
        with open(log_path, "a") as f:
            f.write("App launched and wrote to USB successfully.\n")
        
        messagebox.showinfo("Success", f"1. Clipboard set to 'CLIPBOARD_SUCCESS'\n2. Log written to: {log_path}\n\nIf you see this, the tool works!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

root = tk.Tk()
root.title("USB Stealth Test")
root.geometry("300x150")

label = tk.Label(root, text="Click to test PC restrictions:", pady=20)
label.pack()

test_btn = tk.Button(root, text="Run Compatibility Test", command=run_test)
test_btn.pack()

root.mainloop()